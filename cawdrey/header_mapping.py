#!/usr/bin/env python
#
#  header_mapping.py
"""
:class:`collections.abc.MutableMapping` which supports duplicate, case-insentive keys.

.. versionadded:: 0.4.0
"""
#
#  Copyright © 2021-2022 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Based on CPython.
#  Licensed under the Python Software Foundation License Version 2.
#  Copyright © 2001-2021 Python Software Foundation. All rights reserved.
#  Copyright © 2000 BeOpen.com. All rights reserved.
#  Copyright © 1995-2000 Corporation for National Research Initiatives. All rights reserved.
#  Copyright © 1991-1995 Stichting Mathematisch Centrum. All rights reserved.
#

# stdlib
from typing import Iterator, List, MutableMapping, Optional, Tuple, Union, cast, overload

# 3rd party
from domdf_python_tools.stringlist import DelimitedList

# this package
from cawdrey.base import VT, T

__all__ = ["HeaderMapping"]


class HeaderMapping(MutableMapping[str, VT]):
	"""
	Provides a :class:`~collections.abc.MutableMapping` interface to a list of headers,
	such as those used in an email message.

	.. seealso:: :class:`email.message.Message` and :class:`email.message.EmailMessage`

	:class:`~collections.abc.MutableMapping` interface,
	which assumes there is exactly one occurrence of the header per mapping.
	Some headers do in fact appear multiple times,
	and for those headers you must use the :meth:`~.HeaderMapping.get_all` method
	to obtain all values for that key.
	"""  # noqa: D400

	def __init__(self):
		self._headers: List[Tuple[str, VT]] = []

	#
	# MAPPING INTERFACE (partial)
	#

	def __len__(self) -> int:
		"""
		Return the total number of keys, including duplicates.
		"""

		return len(self._headers)

	def __getitem__(self, name: str) -> VT:
		"""
		Get a header value.

		.. note::

			If the header appears multiple times, exactly which occurrence gets returned is undefined.
			Use the :meth:`~.HeaderMapping.get_all` method to get all values matching a header field name.

		:param name:
		"""

		if name not in self:
			raise KeyError(name)

		return cast(VT, self.get(name))

	def __setitem__(self, name: str, val: VT) -> None:
		"""
		Set the value of a header.

		.. attention:

			This does not overwrite existing headers with the same field name.
			Use :meth:`HeaderMapping.__delitem__` first to delete any existing headers.

		:param name:
		:param val:
		"""

		self._headers.append((name, val))

	def __delitem__(self, name: str) -> None:
		"""
		Delete all occurrences of a header, if present.

		Does not raise an exception if the header is missing.

		:param name:
		"""

		name = name.lower()
		newheaders = []

		for k, v in self._headers:
			if k.lower() != name:
				newheaders.append((k, v))

		self._headers = newheaders

	def __contains__(self, name: object) -> bool:
		"""
		Returns whether ``name`` is in the :class:`~.HeaderMapping`.

		:param name:

		:rtype:

		.. latex:clearpage::
		"""

		if not isinstance(name, str):
			return False

		name = name.lower()

		for k, v in self._headers:
			if k.lower() == name:
				return True

		return False

	def __iter__(self) -> Iterator[str]:
		"""
		Returns an iterator over the keys in the :class:`~.HeaderMapping`.
		"""

		for field, value in self._headers:
			yield field

	def keys(self) -> List[str]:  # type: ignore
		"""
		Return a list of all the message's header field names.

		These will be sorted in the order they appeared in the original message,
		or were added to the message, and may contain duplicates.
		Any fields deleted and re-inserted are always appended to the header list.
		"""

		return [k for k, v in self._headers]

	def values(self) -> List[VT]:  # type: ignore
		"""
		Return a list of all the message's header values.

		These will be sorted in the order they appeared in the original message,
		or were added to the message, and may contain duplicates.
		Any fields deleted and re-inserted are always appended to the header list.
		"""

		return [v for k, v in self._headers]

	def items(self) -> List[Tuple[str, VT]]:  # type: ignore
		"""
		Get all the message's header fields and values.

		These will be sorted in the order they appeared in the original message,
		or were added to the message, and may contain duplicates.
		Any fields deleted and re-inserted are always appended to the header list.
		"""

		return self._headers[:]

	@overload
	def get(self, k: str) -> Optional[VT]: ...

	@overload
	def get(self, k: str, default: Union[VT, T]) -> Union[VT, T]: ...

	def get(self, k: str, default=None):
		"""
		Get a header value.

		Like :meth:`~.HeaderMapping.__getitem__`,
		but returns ``default`` instead of :py:obj:`None` when the field is missing.

		:param k:
		:param default:
		"""

		name = k.lower()

		for k, v in self._headers:
			if k.lower() == name:
				return v

		return default

	#
	# Additional useful stuff
	#

	@overload
	def get_all(self, k: str) -> Optional[List[VT]]: ...

	@overload
	def get_all(self, k: str, default: Union[VT, T]) -> Union[List[VT], T]: ...

	def get_all(self, k: str, default=None):
		"""
		Return a list of all the values for the named field.

		These will be sorted in the order they appeared in the original message,
		and may contain duplicates.
		Any fields deleted and re-inserted are always appended to the header list.

		If no such fields exist, ``default`` is returned.

		:param k:
		:param default:
		"""

		values = []
		name = k.lower()

		for k, v in self._headers:
			if k.lower() == name:
				values.append(v)

		if not values:
			return default

		return values

	def __repr__(self) -> str:
		"""
		Return a string representation of the :class:`~.HeaderMapping`.

		.. versionadded:: 0.4.1
		"""

		items = DelimitedList([f"{k!r}: {v!r}" for k, v in self.items()])
		as_dict = f"{{{items:, }}}"

		return f"<{self.__class__.__name__}({as_dict})>"
