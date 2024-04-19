from abc import ABC, abstractmethod

import pandas as pd


class AbstractAnalyzer(ABC):
    """
    分析器抽象函数
    """
    context = None

    def set_context(self, context):
        """
        设置回测的上下文对象
        :param context:
        :return:
        """
        self.context = context
        return self

    @abstractmethod
    def start(self):
        """
        在回测开始之前调用,对应第0根bar
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def next(self):
        """
        策略正常运行阶段, 每个Bar执行一次
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        """
        策略结束时执行
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def get_analysis(self):
        """
        获取分析器结果
        :return:
        """
        raise NotImplementedError


class TimeReturn(AbstractAnalyzer):
    """
    获取Portfolio的收益情况
    """

    def __init__(self):
        # datetimes
        self.datetimes = []
        # 持仓市值
        self.market_values = []
        # 现金
        self.cash = []
        # Portfolio total value
        self.total_values = []
        # Portfolio returns
        self.returns = []
        # profit and loss
        self.pnls = []
        # benchmark close price
        self.benchmarks = []
        # benchmark returns
        self.bchmk_returns = []

    def start(self):
        pass

    def next(self):
        if self.context.unit in ['1m', '5m']:
            self.datetimes.append(self.context.current_dt.strftime('%Y-%m-%d %H:%M:%S'))
        else:
            self.datetimes.append(self.context.current_dt.strftime('%Y-%m-%d'))

        # 计算收益率
        market_value = self.context.portfolio.positions_value
        cash = self.context.portfolio.available_cash
        self.market_values.append(market_value)
        self.cash.append(cash)

        total_value = market_value + cash
        benchmark_value = self.context.benchmark_value
        if len(self.total_values) > 0:
            self.pnls.append(total_value - self.total_values[-1])
            self.returns.append(total_value/self.total_values[-1] - 1)
            self.bchmk_returns.append(benchmark_value/self.benchmarks[-1] - 1)
        else:
            self.pnls.append(0.0)
            self.returns.append(0.0)
            self.bchmk_returns.append(0.0)

        # 保存当前total value
        self.total_values.append(total_value)

        # 保存benchmark price
        self.benchmarks.append(benchmark_value)

    def stop(self):
        pass

    def get_analysis(self):
        return {"returns": pd.Series(self.returns, index=self.datetimes, name='returns'),
                "total_values": pd.Series(self.total_values, self.datetimes, name='total_values'),
                "market_values": pd.Series(self.market_values, self.datetimes, name='market_values'),
                "cash": pd.Series(self.cash, self.datetimes, name='cash'),
                "pnls": pd.Series(self.pnls, self.datetimes, name='pnls'),
                "bchmk_returns": pd.Series(self.bchmk_returns, self.datetimes, name='bchmk_returns'),
                }
