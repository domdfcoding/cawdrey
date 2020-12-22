#!/usr/bin/env python
#
#  frozenordereddict.py
"""
Provides FrozenOrderedDict, an immutable ordered dictionary.
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#  Copyright (c) 2015 Warren Smith
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

# stdlib
import operator
from collections import OrderedDict
from functools import reduce
from typing import AbstractSet, Optional, Tuple, TypeVar, Union, ValuesView, overload

# this package
from .base import KT, VT, FrozenBase

__all__ = ["FrozenOrderedDict"]

T = TypeVar('T')


class FrozenOrderedDict(FrozenBase[KT, VT]):
	"""
	An immutable OrderedDict.
	It can be used as a drop-in replacement for dictionaries where immutability is desired.
	"""

	dict_cls = OrderedDict

	def __init__(self, *args, **kwargs):
		if hasattr(self, "_dict"):
			raise TypeError(f"`{self.__class__}` can only be initialised once.")

		super().__init__(*args, **kwargs)

	def copy(self, *args, **kwargs):
		"""
		Return a copy of the :class:`~cawdrey.frozenordereddict.FrozenOrderedDict`.

		:param args:
		:param kwargs:
		"""

		new_dict = self._dict.copy()

		if args or kwargs:
			new_dict.update(OrderedDict(*args, **kwargs))

		return self.__class__(new_dict)

	def __hash__(self) -> int:
		"""
		Return :func:`hash(self) <hash>`.
		"""

		if self._hash is None:
			self._hash = reduce(operator.xor, map(hash, self.items()), 0)

		return self._hash

	@overload
	def get(self, k: KT) -> Optional[VT]:
		...  # pragma: no cover

	@overload
	def get(self, k: KT, default: Union[VT, T]) -> Union[VT, T]:
		...  # pragma: no cover

	def get(self, k, default=None):
		"""
		Return the value for ``k`` if ``k`` is in the dictionary, else ``default``.

		:param k: The key to return the value for.
		:param default: The value to return if ``key`` is not in the dictionary.
		"""

		return super().get(k, default)

	def items(self) -> AbstractSet[Tuple[KT, VT]]:
		r"""
		Returns a set-like object providing a view on the :class:`~.FrozenOrderedDict`\'s items.
		"""

		return super().items()

	def keys(self) -> AbstractSet[KT]:
		r"""
		Returns a set-like object providing a view on the :class:`~.FrozenOrderedDict`\'s keys.
		"""

		return super().keys()

	def values(self) -> ValuesView[VT]:
		r"""
		Returns an object providing a view on the :class:`~.FrozenOrderedDict`\'s values.
		"""

		return super().values()

	def __contains__(self, key: object) -> bool:
		"""
		Return ``key in self``.

		:param key:
		"""

		return super().__contains__(key)

	def __getitem__(self, key: KT) -> VT:
		"""
		Return ``self[key]``.

		:param key:
		"""

		return super().__getitem__(key)
