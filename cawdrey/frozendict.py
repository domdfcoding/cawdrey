#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  frozendict.py
"""
Provides frozendict, a simple immutable dictionary.
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#  Copyright (c) Marco Sulla
#  Copyright (c) 2012 Santiago Lezica
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

# this package
from .base import FrozenBase


class frozendict(FrozenBase):
	"""
	An immutable wrapper around dictionaries that implements the complete
	:py:class:`collections.Mapping` interface. It can be used as a
	drop-in replacement for dictionaries where immutability is desired.
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

	def sorted(self, *args, by="keys", **kwargs):
		"""
		Return a new `frozendict`, with the element insertion sorted.
		The signature is the same of builtin `sorted()` function, except for
		the additional parameter `by`, that is "keys" by default and can also
		be "values" and "items". So the resulting `frozendict` can be sorted
		by keys, values or items.

		If you want more complicated sorts, see the documentation of
		`sorted()`. Take into mind that the parameters passed to the `key`
		function are the keys of the `frozendict` if `by == "keys"`, and are
		the items otherwise.

		PS: Note that sort by keys and items are identical. The only
		difference is when you want to customize the sorting passing a custom
		`key` function. You *could* achive the same result using
		`by="values"`, since also sorting by values passes the items to the
		key function. But this is an implementation detail and you should not
		rely on it.
		"""

		if not self:
			return self

		sort_by_keys = by == "keys"
		sort_by_values = by == "values"

		if sort_by_keys:
			tosort = self.keys()
		elif sort_by_values:
			tosort = self.items()
		elif by == "items":
			tosort = self.items()
		else:
			raise ValueError(f"Unexpected value for parameter `by`: {by}")

		if sort_by_values:
			kwargs.setdefault("key", lambda item: item[1])

		it_sorted = sorted(tosort, *args, **kwargs)

		if it_sorted == list(tosort):
			return self

		if sort_by_keys:
			res = {k: self[k] for k in it_sorted}
		else:
			res = it_sorted

		return self.__class__(res)

	def __add__(self, other, *args, **kwargs):
		"""
		If you add a dict-like object, a new frozendict will be returned, equal
		to the old frozendict updated with the other object.
		"""

		tmp = dict(self)

		try:
			tmp.update(other)
		except Exception:
			msg = f"Unsupported operand type(s) for +: `{self.__class__.__name__}` and `{other.__class__.__name__}`"
			raise TypeError(msg) from None

		return self.__class__(tmp)

	def __sub__(self, other, *args, **kwargs):
		"""
		The method will create a new `frozendict`, result of the subtraction
		by `other`.

		If `other` is a `dict`-like, the result will have the items of the
		`frozendict` that are *not* in common with `other`.

		If `other` is another type of iterable, the result will have the
		items of `frozendict` without the keys that are in `other`.
		"""

		try:
			iter(other)
		except Exception:
			msg = f"Unsupported operand type(s) for -: `{self.__class__.__name__}` and `{other.__class__.__name__}`"
			raise TypeError(msg) from None

		try:
			res = {k: v for k, v in self.items() if (k, v) not in other.items()}
		except Exception:
			if not hasattr(other, "gi_running"):
				true_other = other
			else:
				true_other = tuple(other)

			res = {k: v for k, v in self.items() if k not in true_other}

		return self.__class__(res)

	def __and__(self, other, *args, **kwargs):
		"""
		Returns a new `frozendict`, that is the intersection between `self`
		and `other`.

		If `other` is a `dict`-like object, the intersection will contain
		only the *items* in common.

		If `other` is another iterable, the intersection will contain
		the items of `self` which keys are in `other`.

		Iterables of pairs are *not* managed differently. This is for
		consistency.

		Beware! The final order is dictated by the order of `other`. This
		allows the coder to change the order of the original `frozendict`.

		The last two behaviors breaks voluntarly the `dict.items()` API, for
		consistency and practical reasons.
		"""

		try:
			try:
				res = {k: v for k, v in other.items() if (k, v) in self.items()}
			except Exception:
				res = {k: self[k] for k in other if k in self}
		except Exception:
			msg = f"Unsupported operand type(s) for &: `{self.__class__.__name__}` and `{other.__class__.__name__}`"
			raise TypeError(msg) from None

		return self.__class__(res)
