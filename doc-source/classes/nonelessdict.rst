==============
NonelessDict
==============

About
========

:class:`~cawdrey.nonelessdict.NonelessDict` is a wrapper around dict that will check if a value is :py:obj:`None`/empty/:py:obj:`False`, and not add the key in that case.

The class has a method :meth:`~cawdrey.nonelessdict.NonelessDict.set_with_strict_none_check` that can be used to set a value and check only for ``None`` values.

:class:`~cawdrey.nonelessdict.NonelessOrderedDict` is based on :class:`~cawdrey.nonelessdict.NonelessDict` and :class:`~python:collections.OrderedDict`, so the order of key insertion is preserved.


API Reference
===========================

.. automodule:: cawdrey.nonelessdict
	:inherited-members:
	:exclude-members: dict_cls

Copyright
=========

| Based on https://github.com/slezica/python-frozendict and https://github.com/jerr0328/python-helpfuldicts .
| Copyright (c) 2012 Santiago Lezica
| Licensed under the MIT License:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
