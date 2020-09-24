#!/usr/bin/env python
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
from abc import abstractmethod
from typing import (
		AbstractSet,
		Any,
		Iterable,
		Iterator,
		Mapping,
		MutableMapping,
		Optional,
		Tuple,
		Type,
		TypeVar,
		Union,
		ValuesView,
		overload
		)

# 3rd party
from domdf_python_tools.doctools import is_documented_by, prettify_docstrings

__all__ = ["DictWrapper", "FrozenBase", "MutableBase"]

KT = TypeVar("KT")
VT = TypeVar("VT")
T = TypeVar('T')


@prettify_docstrings
class DictWrapper(Mapping[KT, VT]):
	"""
	Abstract Mixin class for classes that wrap a dict object or similar
	"""

	_dict: dict

	def __getitem__(self, key: KT) -> VT:
		"""
		Return ``self[key]``.

		:param key:
		"""

		return self._dict[key]

	def __contains__(self, key: object) -> bool:
		"""
		Return ``key in self``.

		:param key:
		"""

		return key in self._dict

	def __iter__(self) -> Iterator[KT]:
		"""
		Iterates over the dictionary's keys
		"""

		return iter(self._dict)

	def __len__(self) -> int:
		"""
		Returns the number of keys in the dictionary.
		"""

		return len(self._dict)

	def __repr__(self) -> str:
		return f"<{self.__class__.__name__} {self._dict!r}>"

	@abstractmethod
	def copy(self, *args, **kwargs):
		pass

	def __copy__(self, *args, **kwargs):
		return self.copy()

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
		"""
		Returns a set-like object providing a view on the :class:`~.bdict`\'s items.
		"""

		return super().items()

	def keys(self) -> AbstractSet[KT]:
		"""
		Returns a set-like object providing a view on the :class:`~.bdict`\'s keys.
		"""

		return super().keys()

	def values(self) -> ValuesView[VT]:
		"""
		Returns an object providing a view on the :class:`~.bdict`\'s values.
		"""

		return super().values()


_T = TypeVar("_T")
_S = TypeVar("_S")


class FrozenBase(DictWrapper[KT, VT]):
	"""
	Abstract Base Class for Frozen dictionaries

	Used by :class:`~.frozendict` and :class:`~.FrozenOrderedDict`.

	Custom subclasses must implement at a minimum ``__init__``,
	``copy``, ``fromkeys``.
	"""

	dict_cls: Optional[Type] = None

	@abstractmethod
	def __init__(self, *args, **kwargs):
		self._dict = self.dict_cls(*args, **kwargs)  # type: ignore
		self._hash = None

	@classmethod
	@overload
	def fromkeys(cls, iterable: Iterable[_T]) -> "FrozenBase[_T, Any]":
		...  # pragma: no cover

	@classmethod
	@overload
	def fromkeys(cls, iterable: Iterable[_T], value: _S) -> "FrozenBase[_T, _S]":
		...  # pragma: no cover

	@classmethod
	@is_documented_by(dict.fromkeys)
	def fromkeys(cls, iterable: Iterable[_T], value: _S = None):
		return cls(dict.fromkeys(iterable, value))


class MutableBase(DictWrapper[KT, VT], MutableMapping[KT, VT]):
	"""
	Abstract Base Class for mutable dictionaries

	Used by :class:`~.NonelessDict` and :class:`~.NonelessOrderedDict`.

	Custom subclasses must implement at a minimum ``__init__``,
	``copy``, ``fromkeys``.
	"""

	dict_cls = None  # type: ignore

	@abstractmethod
	def __init__(self, *args, **kwargs):
		self._dict = self.dict_cls(*args, **kwargs)  # type: ignore
		self._hash = None

	def __setitem__(self, key, value):
		if value:
			self._dict[key] = value

	def __delitem__(self, key):
		del self._dict[key]

	@classmethod
	@overload
	def fromkeys(cls, iterable: Iterable[_T]) -> "MutableBase[_T, Any]":
		...  # pragma: no cover

	@classmethod
	@overload
	def fromkeys(cls, iterable: Iterable[_T], value: _S) -> "MutableBase[_T, _S]":
		...  # pragma: no cover

	@classmethod
	@is_documented_by(dict.fromkeys)
	def fromkeys(cls, iterable: Iterable[_T], value: _S = None):
		return cls(dict.fromkeys(iterable, value))
