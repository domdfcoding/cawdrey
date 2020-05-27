#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  __init__.py
"""
Provides several useful custom dictionaries
"""
#
#  Copyright (c) 2019-2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
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

from .alphadict import alphabetical_dict, AlphaDict
from .base import FrozenBase, MutableBase
from .bdict import bdict
from .frozendict import frozendict
from .nonelessdict import NonelessDict, NonelessOrderedDict
from .frozenordereddict import FrozenOrderedDict

__author__ = "Dominic Davis-Foster"
__copyright__ = "2020 Dominic Davis-Foster"

__license__ = "LGPLv3+"
__version__ = "0.1.4"
__email__ = "dominic@davis-foster.co.uk"

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
	]
