#!/usr/bin/env python
#
#  utils.py
"""
General utility functions.
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
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

# stdlib
import re
from typing import Any, Dict, Pattern, Union

__all__ = ["search_dict"]


def search_dict(dictionary: Dict[str, Any], regex: Union[str, Pattern]) -> Dict[str, Any]:
	"""
	Return the subset of the dictionary whose keys match the regex.

	:param dictionary:
	:param regex:
	"""

	if not isinstance(regex, Pattern):
		regex = re.compile(regex)

	return {key: value for key, value in dictionary.items() if regex.match(key)}
