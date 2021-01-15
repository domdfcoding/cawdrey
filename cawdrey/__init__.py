#!/usr/bin/env python
#
#  __init__.py
"""
Provides several useful custom dictionaries.
"""
#
#  Copyright © 2019-2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#  Copyright © 2015 Warren Smith
#  Copyright © Marco Sulla
#  Copyright © 2012 Santiago Lezica
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
from ._bdict import bdict
from ._frozendict import frozendict
from .alphadict import AlphaDict, alphabetical_dict
from .base import FrozenBase, MutableBase
from .frozenordereddict import FrozenOrderedDict
from .nonelessdict import NonelessDict, NonelessOrderedDict
from .tally import Tally

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2020 Dominic Davis-Foster"
__license__: str = "LGPLv3+"
__version__: str = "0.3.0"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = [
		"__version__",
		"alphabetical_dict",
		"AlphaDict",
		"bdict",
		"FrozenBase",
		"frozendict",
		"FrozenOrderedDict",
		"MutableBase",
		"NonelessDict",
		"NonelessOrderedDict",
		"Tally",
		]
