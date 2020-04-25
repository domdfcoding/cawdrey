==========
Cawdrey
==========

.. image:: https://travis-ci.org/domdfcoding/cawdrey.svg?branch=master
	:target: https://travis-ci.org/domdfcoding/cawdrey
	:alt: Build Status
.. image:: https://readthedocs.org/projects/cawdrey/badge/?version=latest
	:target: https://cawdrey.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status
.. image:: https://img.shields.io/pypi/v/cawdrey.svg
	:target: https://pypi.org/project/cawdrey/
	:alt: PyPI
.. image:: https://img.shields.io/pypi/pyversions/cawdrey.svg
	:target: https://pypi.org/project/cawdrey/
	:alt: PyPI - Python Version
.. image:: https://coveralls.io/repos/github/domdfcoding/cawdrey/badge.svg?branch=master
	:target: https://coveralls.io/github/domdfcoding/cawdrey?branch=master
	:alt: Coverage
.. image:: https://img.shields.io/badge/License-LGPL%20v3-blue.svg
	:alt: PyPI - License
	:target: https://github.com/domdfcoding/cawdrey/blob/master/LICENSE


A collection of useful custom dictionaries for Python.

Contents
##########

	* ``frozendict``: An immutable dictionary that cannot be changed after creation.
	* ``FrozenOrderedDict``: An immutable ``OrderedDict`` where the order of keys is preserved, but that cannot be changed after creation.
	* ``AlphaDict``: A ``FrozenOrderedDict`` where the keys are stored in alphabetical order.
	* ``bdict``: A dictionary where `key, value` pairs are stored both ways round.

|

This package also provides two base classes for creating your own custom dictionaries:

	* ``FrozenBase``: An Abstract Base Class for Frozen dictionaries.

	* ``MutableBase``: An Abstract Base Class for mutable dictionaries.

|

Other Dictionary Packages
===========================

If you're looking to unflatten a dictionary, such as to go from this:

.. code-block:: python

	{'foo.bar': 'val'}

to this:

.. code-block:: python
	{'foo': {'bar': 'val'}}

check out `unflatten`_, `flattery`_ or `morph`_  to accomplish that.

.. _unflatten: https://github.com/dairiki/unflatten
.. _morph: https://github.com/metagriffin/morph
.. _flattery: https://github.com/acg/python-flattery

There's also `python-benedict`_, which provides a custom dictionary with **keylist/keypath** support, **I/O** shortcuts (``Base64``, ``CSV``, ``JSON``, ``TOML``, ``XML``, ``YAML``, ``pickle``, ``query-string``) and many **utilities**.

.. _python-benedict: https://github.com/fabiocaccamo/python-benedict

|


And Finally:
==============

`Why Cawdrey? <https://en.wikipedia.org/wiki/Robert_Cawdrey>`_
