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

# stdlib
import collections
import sys
from numbers import Real
from typing import Counter, Dict, Optional, TypeVar, Union, overload

# this package
from cawdrey.base import KT

__all__ = ["Tally"]

_F = TypeVar("_F", bound=Real)

if sys.version_info < (3, 8):  # pragma: no cover (py38+)
	Percentage = Dict[KT, float]
else:  # pragma: no cover (<py38)
	# stdlib
	from typing import OrderedDict

	Percentage = OrderedDict[KT, float]


class Tally(Counter[KT]):
	"""
	Subclass of :class:`collections.Counter` with additional methods.

	.. versionadded:: 0.3.0
	"""

	def as_percentage(self) -> Percentage:
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
		return collections.OrderedDict((i, count / total) for i, count in self.most_common())

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
