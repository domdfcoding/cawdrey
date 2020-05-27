#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nonelessdict.py
"""
Provides frozendict, a simple immutable dictionary.
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#  Copyright (c) Jeremy Mayeres
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

# this package
from .base import MutableBase


class NonelessDict(MutableBase):
	"""
	A wrapper around dict that will check if a value is None/empty/False,
	and not add the key in that case.
	Use the set_with_strict_none_check function to check only for None
	"""

	dict_cls = dict

	def __init__(self, *args, **kwargs):
		if hasattr(self, "_dict"):
			raise TypeError(f"`{self.__class__}` can only be initialised once.")

		super().__init__(*args, **kwargs)

	def copy(self, **add_or_replace):
		return self.__class__(self, **add_or_replace)

	def __hash__(self):
		if self._hash is None:
			h = 0
			for key, value in self._dict.items():
				h ^= hash((key, value))
			self._hash = h
		return self._hash

	def set_with_strict_none_check(self, key, value):
		if value is not None:
			self._dict[key] = value


class NonelessOrderedDict(MutableBase):
	"""
	A wrapper around OrderedDict that will check if a value is None/empty/False,
	and not add the key in that case.
	Use the set_with_strict_none_check function to check only for None
	"""

	dict_cls = OrderedDict

	def __init__(self, *args, **kwargs):
		if hasattr(self, "_dict"):
			raise TypeError(f"`{self.__class__}` can only be initialised once.")

		super().__init__(*args, **kwargs)

	def copy(self, *args, **kwargs):
		new_dict = self._dict.copy()

		if args or kwargs:
			new_dict.update(OrderedDict(*args, **kwargs))

		return self.__class__(new_dict)

	def __hash__(self):
		if self._hash is None:
			self._hash = reduce(operator.xor, map(hash, self.items()), 0)

		return self._hash

	def set_with_strict_none_check(self, key, value):
		if value is not None:
			self._dict[key] = value
