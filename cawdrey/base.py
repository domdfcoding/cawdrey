#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  base.py
"""
Base Classes
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#  Copyright (c) 2015 Warren Smith
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

# stdlib
from abc import ABC, abstractmethod
from collections.abc import Mapping, MutableMapping

# 3rd party
from domdf_python_tools.doctools import is_documented_by


class DictWrapper(ABC):
	"""
	Absrtract Mixin class for classes that wrap a dict object or similar
	"""

	def __getitem__(self, key):
		return self._dict[key]

	def __contains__(self, key):
		return key in self._dict

	def __iter__(self):
		return iter(self._dict)

	def __len__(self):
		return len(self._dict)

	def __repr__(self):
		return f'<{self.__class__.__name__} {self._dict!r}>'

	@abstractmethod
	def copy(self, *args, **kwargs):
		pass

	def __copy__(self, *args, **kwargs):
		return self.copy()


class FrozenBase(DictWrapper, Mapping):
	"""
	Abstract Base Class for Frozen dictionaries

	Used by frozendict and FrozenOrderedDict.

	Custom subclasses must implement at a minimum ``__init__``,
	``copy``, ``fromkeys``.
	"""

	dict_cls = None

	@abstractmethod
	def __init__(self, *args, **kwargs):
		self._dict = self.dict_cls(*args, **kwargs)
		self._hash = None

	@classmethod
	@is_documented_by(dict.fromkeys)
	def fromkeys(cls, *args, **kwargs):
		return cls(dict.fromkeys(*args, **kwargs))


class MutableBase(DictWrapper, MutableMapping):
	"""
	Abstract Base Class for mutable dictionaries

	Used by NonelessDict and NonelessOrderedDict.

	Custom subclasses must implement at a minimum ``__init__``,
	``copy``, ``fromkeys``.
	"""

	dict_cls = None

	@abstractmethod
	def __init__(self, *args, **kwargs):
		self._dict = self.dict_cls(*args, **kwargs)
		self._hash = None

	def __setitem__(self, key, value):
		if value:
			self._dict[key] = value

	def __delitem__(self, key):
		del self._dict[key]

	@classmethod
	@is_documented_by(dict.fromkeys)
	def fromkeys(cls, *args, **kwargs):
		return cls(dict.fromkeys(*args, **kwargs))
