from six import with_metaclass
import abc
from typing import Callable


class AbstractPosition(with_metaclass(abc.ABCMeta)):
    @property
    @abc.abstractmethod
    def stock_code(self) -> str:
        """
        标的代码
        :return:
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def open_price(self):
        """
        平均建仓成本
        :return:
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def can_use_volume(self):
        """
        可用数量
        :return:
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def volume(self):
        """
        持仓数量
        :return:
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def value(self):
        """
        市值
        :return:
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def init_time(self):
        """
        建仓时间
        :return:
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def init_date(self):
        """
        减仓日期
        :return:
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def transact_time(self):
        """
        最后交易时间
        :return:
        """
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def transact_date(self):
        """
        最后交易日期
        :return:
        """
        raise NotImplementedError
