import datetime
from typing import Callable
from pqsdk.api import is_open_trade_date, get_next_trading_date


class TimerFactory:
    def __init__(self, unit: str):
        """
        行情周期单位： 1d, 1m, 5m
        :param unit:
        """
        self.unit = unit      # 回测运行中基准行情的单位
        self.timer_list = []  # 定时器字典列表
        self.carry_dict = {}  # 顺延下一个交易日运行的timer {index: timer}
        self.timer_index = 0  # 给每个定时器一个编号

    @classmethod
    def format_time_str(cls, time_str):
        """
        字符串time_str作为输入，并返回格式化为HH:MM:SS的字符串，如果输入为HH:MM格式，则自动补充为HH:MM:00
        :param time_str:
        :return:
        """
        parts = time_str.split(':')
        if len(parts) == 2:
            # 如果是'HH:MM'格式，则自动补充为'HH:MM:00'
            return f"{parts[0]}:{parts[1]}:00"
            # 如果不是'HH:MM'格式，则检查是否是'HH:MM:SS'格式
        elif len(parts) == 3:
            # 如果是'HH:MM:SS'格式，则直接返回原字符串
            return time_str
        else:
            # 如果不是期望的格式，则返回错误或空字符串
            raise Exception(f"字符串格式不符合: {time_str}, 必须为HH:MM格式，或者HH:MM:SS的格式")

    def add_timer(self,
                  callback: Callable,
                  kwargs,
                  when='00:00:00',
                  weekdays=None,
                  weekcarry=False,
                  monthdays=None,
                  monthcarry=True,
                  ):
        """
        添加计时器

        :param callback: 回调函数
        :param kwargs: 回调函数的参数
        :param when: 运行时间, format: '%H:%M:%S'
        :param weekdays: 每星期的第几天运行, Monday is 1, Sunday is 7
        :param weekcarry: weekday为非交易日，是否顺延下一个交易日
        :param monthdays: 每月的第几天运行
        :param monthcarry: 为非交易日，是否顺延下一个交易日
        :return:
        """
        # 格式化为HH:MM:SS的字符串
        when = self.format_time_str(when)

        if monthdays is None:
            monthdays = []
        if weekdays is None:
            weekdays = []

        self.timer_index += 1
        timer = dict(index=self.timer_index,
                     callback=callback,
                     kwargs=kwargs,
                     when=when,
                     weekdays=weekdays,
                     weekcarry=weekcarry,
                     monthdays=monthdays,
                     monthcarry=monthcarry
                     )
        self.timer_list.append(timer)

    def carry_on(self, index, date, callback, kwargs):
        """
        顺延到下一个交易日执行的回调函数
        :param index: 定时器编号
        :param date:
        :param callback: 回调函数
        :param kwargs: 回调函数的参数字典
        :return:
        """
        self.carry_dict[index] = dict(date=date, callback=callback, kwargs=kwargs)

    def notify_timer(self, current_dt: datetime.datetime):
        """
        根据参数日期时间，遍历timer_list, 对符合条件的timer执行callback回调函数
        :param current_dt: 日期时间，datetime类型
        :return:
        """
        for timer in self.timer_list:
            index = timer['index']
            callback = timer['callback']
            kwargs = timer['kwargs']
            weekdays = timer['weekdays']
            weekcarry = timer['weekcarry']
            monthdays = timer['monthdays']
            monthcarry = timer['monthcarry']

            current_date = current_dt.strftime('%Y-%m-%d')

            # 1、先执行顺延的任务
            if index in self.carry_dict:
                carry_timer = self.carry_dict[index]
                # 检查是否顺延执行
                if current_date == carry_timer['date']:
                    # print(f"carry On: index={index}, date={carry_timer['date']}")
                    carry_timer['callback'](**carry_timer['kwargs'])
                    del self.carry_dict[index]  # 删除已经执行的顺延timer

            # 2、执行计划任务
            if not is_open_trade_date(current_date):  # 非交易日
                if len(weekdays) > 0 and current_dt.weekday() + 1 in weekdays and weekcarry:
                    self.carry_on(index, get_next_trading_date(current_date), callback, kwargs)  # 顺延下一个交易日执行

                if len(monthdays) > 0 and current_dt.day in monthdays and monthcarry:
                    self.carry_on(index, get_next_trading_date(current_date), callback, kwargs)  # 顺延下一个交易日执行

                continue

            # 每周运行
            if len(weekdays) > 0 and current_dt.weekday() + 1 not in weekdays:
                continue

            # 每月运行
            if len(monthdays) > 0 and current_dt.day not in monthdays:
                continue

            # 执行回调函数, 如果是基准周期是1d则直接放行，如果是1m或者5m，则时间到达后执行
            if self.unit in ['1d'] or current_dt.strftime('%H:%M:%S') == timer['when']:
                # 碰巧当日也是顺延执行timer的执行日期, callback不需要重复执行
                if index in self.carry_dict and self.carry_dict[index]['date'] == current_date:
                    continue

                callback(**kwargs)



