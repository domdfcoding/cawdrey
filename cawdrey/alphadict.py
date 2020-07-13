#!/usr/bin/env python
#
#  alphadict.py
"""
Provides AlphaDict, a frozen OrderedDict where the keys are stored alphabetically.
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
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
from collections import OrderedDict
from typing import Iterable, Optional

# this package
from .base import KT, VT
from .frozenordereddict import FrozenOrderedDict


def alphabetical_dict(**kwargs):
	"""
	Returns an :class:`~collections.OrderedDict` with the keys sorted alphabetically.

	:param kwargs:
	:type kwargs:

	:return:
	:rtype:
	"""

	return OrderedDict(sorted(kwargs.items()))


class AlphaDict(FrozenOrderedDict[KT, VT]):
	r"""
	Initialize an immutable, Alphabetised dictionary.
	The signature is the same as regular dictionaries.

	dict() -> new empty AlphaDict

	dict(mapping) -> new AlphaDict initialized from a mapping object's (key, value) pairs

	dict(iterable) -> new AlphaDict initialized as if via:

	.. code-block:: python

		d = {}
		for k, v in iterable:
			d[k] = v

	dict(\*\*kwargs) -> new AlphaDict initialized with the name=value pairs in the keyword argument list.
	For example:

	.. code-block::

		dict(one=1, two=2)
	"""

	def __init__(self, seq: Optional[Iterable] = None, **kwargs):
		if seq:
			kwargs = dict(seq)

		super().__init__(sorted(kwargs.items()))
