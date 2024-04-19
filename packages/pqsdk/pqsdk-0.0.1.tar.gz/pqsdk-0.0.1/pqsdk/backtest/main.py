# coding=utf-8
import datetime
import time
import pqsdk.api as api
from pqsdk.utils.dynamic_import import check_module, import_module_from_spec, import_module_from_code
from pqsdk.utils.import_global_modules import import_modules
from pqsdk import log
from .context import StrategyContext
from pqsdk.utils.timer_factory import TimerFactory
import pandas as pd
from .analyzer import TimeReturn
from typing import Callable
import pqsdk.utils.file_util as fu

# 初始化策略前，导入sdk中的所有对象、函数、属性到全局变量中，以支持在策略中调用
import_modules(api)


class BacktestExecutor:
    def __init__(self, kwargs: dict):

        # 策略参数, 从list转换为dict， 根据数据推断，把value转换为正确的数据类型
        # self.strategy_params = {param['key']: convert_to_type(param['value']) for param in kwargs.get('parameters')}
        self.strategy_params = kwargs.get('parameters')

        # # 检查必须的输入参数
        must_have_params = {'benchmark': "行情基准",
                            'stock_pool': "股票池",
                            'unit': "行情周期",
                            'adjust_period': "调仓周期",
                            'hold_maxsize': "最大持仓",
                            "cash": "回测初始资金",
                            'start_date': "回测开始日期",
                            'end_date': "回测结束日期",
                            }
        for param, desc in must_have_params.items():
            if param not in self.strategy_params:
                content = f"输入参数中缺少必须的参数：{param}: {desc}"
                raise Exception(content)

        # 默认回测参数
        self.params = dict(
            # 股票池 [000300.SH,000905.SH,000852.SH]
            stock_pool=self.strategy_params.get('stock_pool', ['000300.SH', '000905.SH', '000852.SH']),
            # 行情基准-运行周期，支持1d，1m，5m，即根据行情基准-证券代码的k线图，按照1d,1m执行handle_bar()函数
            unit=self.strategy_params.get('unit', '1d'),
            # 除权方式，, 支持none：不复权，front：前复权，back：后复权
            dividend_type=self.strategy_params.get('dividend_type', 'back'),
            strategy_file=kwargs.get('strategy_file', None),  # 策略代码文件
            strategy_script=kwargs.get('script', None),  # 策略代码
            parameters=self.strategy_params,  # dict类型，策略中可以访问到到自定义参数列表
            adjust_period=self.strategy_params.get('adjust_period', 5),  # 调仓周期，结合start_date和end_date计算调仓日列表
            hold_maxsize=self.strategy_params.get('hold_maxsize', 10),  # 最大持仓股票数量
            start_date=self.strategy_params.get('start_date'),  # 回测开始日期
            end_date=self.strategy_params.get('end_date'),  # 回测结束日期
            excluded_dates=None,  # 排除不交易的日期
            benchmark=self.strategy_params.get('benchmark', '000300.SH'),  # 回测基准
            init_investment=self.strategy_params.get('cash', 1000000),  # 初始回测资金
            commission=0.0,  # 交易佣金费率
            slip_type="perc",
            slip_perc=0.0,
            slip_fixed=0.0,
            print_dev=True,  # 是否打印开发日志
            save_result=True,  # 是否保存回测结果
            save_path="storage",
            save_tearsheet=True,  # 保存Tear sheet
            save_db=True,
        )

        # 初始化策略程序
        if self.params['strategy_file']:
            module_spec = check_module(self.params['strategy_file'])
            if module_spec:
                self.strategy = import_module_from_spec(module_spec)
                log.debug(f"从文件获取策略对象：strat_path = {self.params['strategy_file']}")
        elif self.params['strategy_script']:
            self.strategy = import_module_from_code(code=self.params['strategy_script'])
            log.info(f"从代码获取策略程序")
        else:
            raise Exception("未找到策略代码，中止回测程序")

        # 自定义定时器工厂
        self.timer_factory = TimerFactory(unit=self.params['unit'])

        # 初始化策略执行的上下文
        self.context = StrategyContext(kwargs=self.params,
                                       timer_factory=self.timer_factory,
                                       notify_order=self.notify_order)

        # 历史委托列表, 从notify_order()函数收集委托数据，回测介绍后写入数据库
        self.orders = []

        # Analyzer dict, key=name, value=analyzer
        self.analyzers = {}

        # 创建文件日志
        file_path = f"{self.params.get('save_path', 'storage')}/logs/"
        fu.create_dir(path=file_path)
        file_name = f'run_backtest_'
        strat_run_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_name += "__time=" + strat_run_time.replace("-", "").replace(":", "").replace(" ", "_") + ".log"
        log_path = file_path + file_name
        # 配置log输出到文件
        log.add_file_handler(name='strategy', file_name=log_path, level=log.DEBUG)

    def add_analyzer(self, name: str, analyzer: Callable):
        self.analyzers[name] = analyzer().set_context(self.context)

    def initialize(self, context):
        """
        初始化方法，在整个回测、模拟实盘中最开始执行一次，用于初始一些全局变量，全局变量会被持久化。重启策略不会再次执行。
        :param context:
        :return:
        """
        if hasattr(self.strategy, 'initialize'):
            self.strategy.initialize(context=context)
        else:
            raise Exception(f"{context.current_dt} 策略中缺少initialize()初始化函数")

    def process_initialize(self, context):
        """
        每次启动策略都会执行的初始化函数，一般用来初始化一些不能持久化保存的内容. , 比如以__开头的全局变量属性，或者计划任务，在 initialize 后执行.
        :param context:
        :return:
        """
        if hasattr(self.strategy, 'process_initialize'):
            self.strategy.process_initialize(context=context)

    def before_trading_start(self, context):
        """
        开盘前运行策略(可选)
        该函数会在每天开始交易前被调用一次, 可以在这里添加一些每天都要初始化的动作。
        该函数依据的时间是股票的交易时间，即该函数启动时间为'09:00'.
        :param context:
        :return:
        """
        if hasattr(self.strategy, 'before_trading_start'):
            self.strategy.before_trading_start(context=context)

    def notify_order(self, order):
        """
        新创建委托的通知
        :param order: 委托的对象
        :return:
        """
        order_dict = {"order_id": order.order_id,
                      "sec_code": order.security,
                      "volume": order.volume,
                      "price": order.price,
                      "is_buy": order.is_buy,
                      "avg_cost": order.avg_cost,
                      "comm": order.commission,
                      "add_time": order.add_time,
                      "trade_date": order.add_time.strftime('%Y-%m-%d')}
        self.orders.append(order_dict)
        log.debug(f"order: {order_dict}")

    def handle_bar(self, context):
        """
        K线处理函数
        :param context:
        :return:
        """
        if hasattr(self.strategy, 'handle_bar'):
            self.strategy.handle_bar(context=context)

    def on_strategy_end(self, context):
        """
        策略结束后执行
        :param context:
        :return:
        """
        if hasattr(self.strategy, 'on_strategy_end'):
            self.strategy.on_strategy_end(context=context)

    @classmethod
    def on_reset(cls, context):
        """
        每日重置的callback函数，必须在before_trading_start()之前执行, 在实盘中，每日早上9:10重置
        :return:
        """
        # --------------------------------------------------------------
        # 重置当日的股票数据字典，包括当日最新价、涨停价、跌停价、是否停牌、是否ST等
        # --------------------------------------------------------------
        context.reset_current_data()
        log.debug(f"{context.current_dt} 策略每日重置完成")

    def run(self):
        """
        执行回测
        :return:
        """
        start_time = time.time()

        # 执行结果
        results = {"benchmark": self.params['benchmark']}

        # 获取行情数据范围
        log.info(f"回测时间范围：start_date={self.params['start_date']}, end_date={self.params['end_date']}")

        # 获取Benchmark Kline, 根据它的Bar进行回测播放
        df = api.get_attribute_history(security=self.params['benchmark'],
                                       fields=['close'],
                                       unit=self.params['unit'],
                                       start_date=self.params['start_date'],
                                       end_date=self.params['end_date'],
                                       dividend_type=self.params['dividend_type'])

        if self.params['unit'] in ['1d']:
            df.index = pd.to_datetime(df.index)

        # 设置context.dt为默认的第一天，因为initialize()或者process_initialize()可能会用到
        self.context.set_dt(df.index[0])

        # 添加默认的analyzer
        self.add_analyzer(name="time_return", analyzer=TimeReturn)

        # 初始化策略, 仅第一次启动策略时执行
        self.initialize(context=self.context)

        # 每次启动策略时执行
        self.process_initialize(context=self.context)

        # 执行Analyzers.start()
        for name, analyzer in self.analyzers.items():
            analyzer.start()

        # 按照回测时间范围的交易日播放进行回测
        trade_date = None
        for trade_time in df.index.tolist():
            # 设置benchmark close price
            self.context.set_benchmark_value(df.loc[trade_time]['close'])

            # 设置context.dt
            if self.context.unit in ['1d']:
                # 如果行情周期unit为天，则回测的当前时间(context.current_dt)指向收盘时间15:00
                close_15_00 = datetime.datetime(trade_time.year, trade_time.month, trade_time.day, 15, 0, 0)
                self.context.set_dt(close_15_00)
            else:
                self.context.set_dt(trade_time)

            # new trade date
            if trade_date is None or trade_time.strftime('%Y-%m-%d') != trade_date:
                trade_date = trade_time.strftime('%Y-%m-%d')
                # 每日重置
                self.on_reset(context=self.context)

                # 每日开盘前，必须执行在定时器任务之前
                self.before_trading_start(context=self.context)

            # 执行定时器任务:run_daily, run_weekly, run_monthly
            self.timer_factory.notify_timer(self.context.current_dt)

            # 按K线图执行
            self.handle_bar(context=self.context)

            # 执行Analyzers.next()
            for name, analyzer in self.analyzers.items():
                analyzer.next()

        # 策略结束
        self.on_strategy_end(context=self.context)

        # 执行Analyzers.stop()
        for name, analyzer in self.analyzers.items():
            analyzer.stop()

        # 获取Analyzers结果
        analysis = {}
        for name, analyzer in self.analyzers.items():
            analysis[name] = analyzer.get_analysis()

        results['analysis'] = analysis

        # 画图数据
        results['plot_data'] = self.context.plot_data

        # 所有委托明细
        orders_df = pd.DataFrame(self.orders)
        results['orders'] = orders_df

        # 总回测时长
        end_time = time.time()
        log.info(f"回测时长(s)： {(end_time - start_time):.2f}")
        # 返回累计收益结果
        returns = results['analysis']['time_return']['returns']
        bchmk_returns = results['analysis']['time_return']['bchmk_returns']
        cum_returns = (1 + returns).cumprod() - 1
        cum_bchmk_returns = (1 + bchmk_returns).cumprod() - 1
        log.info(f"时长(s)={(end_time - start_time):.2f}, "
                 f"策略收益={cum_returns.values.tolist()[-1]} "
                 f"基准收益={cum_bchmk_returns.values.tolist()[-1]} "
                 )

        return results


# ---------------------------------------------------------
# 外部可以访问的列表
# ---------------------------------------------------------
__all__ = ["BacktestExecutor"]
__all__.extend([name for name in globals().keys() if name.startswith("get")])
