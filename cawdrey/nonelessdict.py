#!/usr/bin/env python
#
#  nonelessdict.py
"""
Provides NonelessDict.
"""
#
#  Copyright © 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#  Copyright © Jeremy Mayeres
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
from typing import Optional

# 3rd party
from domdf_python_tools.doctools import prettify_docstrings

# this package
from .base import KT, VT, MutableBase

__all__ = ["NonelessDict", "NonelessOrderedDict"]


@prettify_docstrings
class NonelessDict(MutableBase[KT, VT]):
	"""
	A wrapper around dict that will check if a value is
	:py:obj:`None`/empty/:py:obj:`False`, and not add the key in that case.

	Use the :meth:`~.NonelessDict.set_with_strict_none_check` method to check only
	for :py:obj:`None`.
	"""  # noqa: D400

	dict_cls = dict  # type: ignore

	def __init__(self, *args, **kwargs):
		if hasattr(self, "_dict"):
			raise TypeError(f"`{self.__class__}` can only be initialised once.")

		super().__init__(*args, **kwargs)

	def copy(self, **add_or_replace):
		"""
		Return a copy of the dictionary.
		"""

		return self.__class__(self, **add_or_replace)

	def __hash__(self) -> int:
		if self._hash is None:
			h = 0
			for key, value in self._dict.items():
				h ^= hash((key, value))
			self._hash = h
		return self._hash

	def set_with_strict_none_check(self, key: KT, value: Optional[VT]) -> None:
		"""
		Set ``key`` in the dictionary to ``value``, but skipping :py:obj:`None` values.

		:param key:
		:param value:
		"""

		if value is not None:
			self._dict[key] = value

	def __setitem__(self, key: KT, value: Optional[VT]):
		if value:
			return super().__setitem__(key, value)


@prettify_docstrings
class NonelessOrderedDict(MutableBase[KT, VT]):
	"""
	A wrapper around OrderedDict that will check if a value is None/empty/False,
	and not add the key in that case.
	Use the set_with_strict_none_check function to check only for None
	"""  # noqa: D400

	dict_cls = OrderedDict  # type: ignore

	def __init__(self, *args, **kwargs):
		if hasattr(self, "_dict"):
			raise TypeError(f"`{self.__class__}` can only be initialised once.")

		super().__init__(*args, **kwargs)

	def copy(self, *args, **kwargs):
		"""
		Return a copy of the dictionary.
		"""

		new_dict = self._dict.copy()

		if args or kwargs:
			new_dict.update(OrderedDict(*args, **kwargs))

		return self.__class__(new_dict)

	def __hash__(self) -> int:
		if self._hash is None:
			self._hash = reduce(operator.xor, map(hash, self.items()), 0)

		return self._hash

	def set_with_strict_none_check(self, key: KT, value: Optional[VT]) -> None:
		"""
		Set ``key`` in the dictionary to ``value``, but skipping :py:obj:`None` values.

		:param key:
		:param value:
		"""

		if value is not None:
			self._dict[key] = value

	def __setitem__(self, key: KT, value: Optional[VT]):
		if value:
			return super().__setitem__(key, value)
