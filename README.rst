==========
Cawdrey
==========

.. start shields

.. image:: https://img.shields.io/travis/domdfcoding/cawdrey/master?logo=travis
    :target: https://travis-ci.org/domdfcoding/cawdrey
    :alt: Travis Build Status
.. image:: https://readthedocs.org/projects/cawdrey/badge/?version=latest
    :target: https://cawdrey.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://img.shields.io/pypi/v/cawdrey.svg
    :target: https://pypi.org/project/cawdrey/
    :alt: PyPI
.. image:: https://img.shields.io/pypi/pyversions/cawdrey.svg
    :target: https://pypi.org/project/cawdrey/
    :alt: PyPI - Python Version
.. image:: https://img.shields.io/pypi/wheel/cawdrey
    :target: https://pypi.org/project/cawdrey/
    :alt: PyPI - Wheel
.. image:: https://img.shields.io/pypi/implementation/cawdrey
    :target: https://pypi.org/project/cawdrey/
    :alt: PyPI - Implementation
.. image:: https://img.shields.io/conda/v/domdfcoding/cawdrey
    :alt: Conda
    :target: https://anaconda.org/domdfcoding/cawdrey
.. image:: https://img.shields.io/conda/pn/domdfcoding/cawdrey?label=conda%7Cplatform
    :alt: Conda Platform
    :target: https://anaconda.org/domdfcoding/cawdrey
.. image:: https://coveralls.io/repos/github/domdfcoding/cawdrey/badge.svg?branch=master
    :target: https://coveralls.io/github/domdfcoding/cawdrey?branch=master
    :alt: Coverage

.. image:: https://img.shields.io/github/license/domdfcoding/cawdrey
    :alt: License
    :target: https://github.com/domdfcoding/cawdrey/blob/master/LICENSE
.. image:: https://img.shields.io/github/languages/top/domdfcoding/cawdrey
    :alt: GitHub top language
.. image:: https://img.shields.io/github/commits-since/domdfcoding/cawdrey/v0.1.3
    :target: https://github.com/domdfcoding/cawdrey/pulse
    :alt: GitHub commits since tagged version
.. image:: https://img.shields.io/github/last-commit/domdfcoding/cawdrey
    :target: https://github.com/domdfcoding/cawdrey/commit/master
    :alt: GitHub last commit
.. image:: https://img.shields.io/maintenance/yes/2020
    :alt: Maintenance
.. image:: https://img.shields.io/codefactor/grade/github/domdfcoding/cawdrey
    :target: https://www.codefactor.io/repository/github/domdfcoding/cawdrey
    :alt: CodeFactor Grade

.. end shields

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


`indexed`_ provides an OrederedDict where the values can be accessed by their index as well as by their keys.

.. _indexed: https://github.com/niklasf/indexed.py

There's also `python-benedict`_, which provides a custom dictionary with **keylist/keypath** support, **I/O** shortcuts (``Base64``, ``CSV``, ``JSON``, ``TOML``, ``XML``, ``YAML``, ``pickle``, ``query-string``) and many **utilities**.

.. _python-benedict: https://github.com/fabiocaccamo/python-benedict




And Finally:
==============

`Why Cawdrey? <https://en.wikipedia.org/wiki/Robert_Cawdrey>`_
