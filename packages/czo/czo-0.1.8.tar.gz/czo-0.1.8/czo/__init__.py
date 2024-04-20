"""
辅助测试的一些常用功能
"""
from ._date import FastDate
from ._faker import Faker
from ._net import NetLib
from ._path import DirLib, PathLib
from ._rand import Random

__all__: list[str] = ["FastDate", "Faker",
                      "PathLib", "DirLib", "Random", "NetLib"]
