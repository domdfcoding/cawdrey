# stdlib
from collections import UserDict

# this package
from typing import Iterable, Optional

from cawdrey.base import KT, VT


class bdict(UserDict[KT, VT]):

	def __init__(self, seq: Optional[Iterable] = ..., **kwargs): ...
