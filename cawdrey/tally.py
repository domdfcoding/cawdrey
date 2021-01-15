#!/usr/bin/env python
#
#  tally.py
"""
Subclass of :class:`collections.Counter` with additional methods.

.. versionadded:: 0.3.0
"""
#
#  Copyright © 2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
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
#  most_common method based on CPython.
#  Licensed under the Python Software Foundation License Version 2.
#  Copyright © 2001-2020 Python Software Foundation. All rights reserved.
#  Copyright © 2000 BeOpen.com. All rights reserved.
#  Copyright © 1995-2000 Corporation for National Research Initiatives. All rights reserved.
#  Copyright © 1991-1995 Stichting Mathematisch Centrum. All rights reserved.
#

# stdlib
import heapq
from numbers import Real
from operator import itemgetter
from typing import Counter, Dict, Iterable, List, Optional, Tuple, TypeVar, Union, overload

# 3rd party
from typing_extensions import Protocol, runtime_checkable

# this package
from cawdrey.base import KT

__all__ = ["_F", "SupportsMostCommon", "Tally", "Percentage"]

_F = TypeVar("_F", float, int, Real)


@runtime_checkable
class SupportsMostCommon(Protocol[KT]):
	"""
	:class:`typing.Protocol` for classes which support a :class:`collections.Counter`-like
	:meth:`collections.Counter.most_common` method.
	"""  # noqa: D400

	def items(self) -> Iterable[Tuple[KT, float]]:
		"""
		Returns an iterator over the mapping’s items (as ``(key, value)`` pairs).
		"""  # noqa: D402

		raise NotImplementedError

	def most_common(self, n: Optional[int] = None) -> Union[List[Tuple[KT, float]], List[Tuple[KT, int]]]:
		"""
		List the ``n`` most common elements and their counts from the most common to the least.
		If ``n`` is :py:obj:`None` then list all element counts.

		.. code-block:: python

			>>> Counter('abracadabra').most_common(3)
			[('a', 5), ('b', 2), ('r', 2)]

		:param n:
		"""

		raise NotImplementedError


class Tally(Counter[KT]):
	"""
	Subclass of :class:`collections.Counter` with additional methods.

	.. versionadded:: 0.3.0
	"""

	def as_percentage(self) -> "Percentage[KT]":
		"""
		Returns the :class:`~.Tally` as a :class:`collections.OrderedDict`
		comprising the count for each element as a percentage of the sum of all elements.

		.. important::
			The sum of the dictionary's values may not add up to exactly ``1.0``
			due to limitations of floating-point numbers.
		"""  # noqa: D400

		# Based on https://stackoverflow.com/a/48952797
		# By https://stackoverflow.com/users/271351/cjbarth
		# CC BY-SA 3.0

		total = self.total
		return Percentage((i, count / total) for i, count in self.most_common())

	@property
	def total(self) -> int:
		"""
		Returns the total count for all elements.
		"""

		return sum(self.values())

	@overload
	def get_percentage(self, item: KT) -> Optional[float]:
		...  # pragma: no cover

	@overload
	def get_percentage(self, item: KT, default: _F) -> Union[_F, float]:
		...  # pragma: no cover

	def get_percentage(self, item: KT, default: Optional[_F] = None) -> Union[None, _F, float]:
		"""
		Returns the count for ``item``, as a percentage of the sum of all elements.

		:param item:
		:param default: A default percentage (as a :class:`float`) to return if ``item`` is not in the dictionary.
		"""

		value = self.get(item)

		if value is None:
			return default
		else:
			return value / self.total

	def most_common(self, n: Optional[int] = None) -> List[Tuple[KT, int]]:
		"""
		List the ``n`` most common elements and their counts from the most common to the least.
		If ``n`` is :py:obj:`None` then list all element counts.

		.. code-block:: python

			>>> Tally('abracadabra').most_common(3)
			[('a', 5), ('b', 2), ('r', 2)]

		:param n:
		"""

		return super().most_common(n)


class Percentage(Dict[KT, float]):
	"""
	Provides a dictionary interface, but with :class:`collections.Counter`'s
	:meth:`collections.Counter.most_common` method.

	Represents the return type of :meth:`cawdrey.tally.Tally.as_percentage()`.
	"""  # noqa

	def most_common(self, n: Optional[int] = None) -> List[Tuple[KT, float]]:
		"""
		List the ``n`` most common elements and their counts from the most common to the least.
		If ``n`` is :py:obj:`None` then list all element counts.

		.. code-block:: python

			>>> Tally('abracadabra').as_percentage().most_common(3)
			[('a', 0.45454545454545453), ('b', 0.18181818181818182), ('r', 0.18181818181818182)]

		:param n:
		"""

		# Emulate Bag.sortedByCount from Smalltalk
		if n is None:
			return sorted(self.items(), key=itemgetter(1), reverse=True)

		return heapq.nlargest(n, self.items(), key=itemgetter(1))
