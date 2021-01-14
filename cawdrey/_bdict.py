#!/usr/bin/env python
#
#  bdict.py
"""
Provides bdict, a dictionary where keys and values are also stored the other way round.
"""
#
#  Copyright © 2019-2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#  Improved May 2020 with suggestions from
#      https://treyhunner.com/2019/04/why-you-shouldnt-inherit-from-list-and-dict-in-python/
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
from collections import UserDict
from typing import AbstractSet, Any, Iterable, Optional, Tuple, TypeVar, Union, ValuesView, overload

# this package
from cawdrey.base import KT, VT, T

__all__ = ["bdict"]


class bdict(UserDict):
	"""
	Returns a new dictionary initialized from an optional positional argument,
	and a possibly empty set of keyword arguments.

	Each ``key: value`` pair is entered into the dictionary in both directions,
	so you can perform lookups with either the key or the value.

	If no positional argument is given, an empty dictionary is created.

	If a positional argument is given and it is a mapping object, a dictionary
	is created with the same key-value pairs as the mapping object.
	Otherwise, the positional argument must be an iterable object.
	Each item in the iterable must itself be an iterable with exactly two
	objects. The first object of each item becomes a key in the new
	dictionary, and the second object the corresponding value.

	If keyword arguments are given, the keyword arguments and their values are
	added to the dictionary created from the positional argument.

	If an attempt is made to add a key or value that already exists in the
	dictionary a :exc:`ValueError` will be raised.

	Keys or values of :py:obj:`None`, :py:obj:`True` and :py:obj:`False` will be stored internally as
	``"_None"``, ``"_True"`` and ``"_False"`` respectively
	"""  # noqa: D400

	# Based on https://stackoverflow.com/a/1063393 by https://stackoverflow.com/users/9493/brian

	# Improved May 2020 with suggestions from
	# https://treyhunner.com/2019/04/why-you-shouldnt-inherit-from-list-and-dict-in-python/

	def __init__(self, seq: Optional[Iterable] = None, **kwargs):
		# if seq and kwargs:
		# 	raise TypeError(f'expected at most 1 arguments, got {len(kwargs)-1:d}')

		super().__init__(seq, **kwargs)
		# if seq:
		# 	for key, value in dict(seq).items():
		# 		self.__setitem__(key, value)
		# else:
		# 	for key, value in kwargs.items():
		# 		self.__setitem__(key, value)

	def __setitem__(self, key, val):
		"""
		Set ``self[key]`` to ``value``.

		:param key:
		:param val:
		"""

		if key in self:
			del self[self[key]]
		if val in self:
			del self[val]
		#
		# if key in self or val in self:
		# 	if key in self and self[key] != val:
		# 		raise ValueError(f"The key '{key}' is already present in the dictionary")
		# 	if val in self and self[val] != key:
		# 		raise ValueError(f"The key '{val}' is already present in the dictionary")

		if key is None:
			key = "_None"
		if val is None:
			val = "_None"

		if isinstance(key, bool):
			if key:
				key = "_True"
			else:
				key = "_False"

		if isinstance(val, bool):
			if val:
				val = "_True"
			else:
				val = "_False"

		self.data[key] = val
		self.data[val] = key

	def __delitem__(self, key: KT):
		"""
		Delete ``self[key]``.

		:param key:
		"""

		value = self.data.pop(key)
		self.data.pop(value, None)

	def __getitem__(self, key: KT) -> VT:
		"""
		Return ``self[key]``.

		:param key:
		"""

		if key is None:
			key = "_None"

		if isinstance(key, bool):
			if key:
				key = "_True"
			else:
				key = "_False"

		val = super().__getitem__(key)

		if val == "_None":
			return None
		elif val == "_True":
			return True
		elif val == "_False":
			return False
		else:
			return val

	def __contains__(self, key: object) -> bool:
		"""
		Return ``key in self``.

		:param key:
		"""

		if key is None:
			key = "_None"

		if isinstance(key, bool):
			if key:
				key = "_True"
			else:
				key = "_False"

		return super().__contains__(key)

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
		Returns a set-like object providing a view on the :class:`~.bdict`\'s items.
		"""

		return super().items()

	def keys(self) -> AbstractSet[KT]:
		r"""
		Returns a set-like object providing a view on the :class:`~.bdict`\'s keys.
		"""

		return super().keys()

	def values(self) -> ValuesView[VT]:
		r"""
		Returns an object providing a view on the :class:`~.bdict`\'s values.
		"""

		return super().values()

	def clear(self) -> None:
		"""
		Removes all items from the :class:`~.bdict`.
		"""

		return super().clear()
