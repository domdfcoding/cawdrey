# stdlib
from collections import UserDict
from typing import Iterable, Optional

# this package
from cawdrey.base import KT, VT


class bdict(UserDict[KT, VT]):

	def __init__(self, seq: Optional[Iterable] = ..., **kwargs): ...
