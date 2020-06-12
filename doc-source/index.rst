==========
Cawdrey
==========

.. start short_desc

**Several useful custom dictionaries**

.. end short_desc
.. start shields 

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs|
	* - Tests
	  - |travis| |requires| |coveralls| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Other
	  - |license| |language| |commits-since| |commits-latest| |maintained| 

.. |docs| image:: https://img.shields.io/readthedocs/cawdrey/latest?logo=read-the-docs
	:target: https://cawdrey.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. |travis| image:: https://img.shields.io/travis/domdfcoding/cawdrey/master?logo=travis
	:target: https://travis-ci.org/domdfcoding/cawdrey
	:alt: Travis Build Status

.. |requires| image:: https://requires.io/github/domdfcoding/cawdrey/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/cawdrey/requirements/?branch=master
	:alt: Requirements Status

.. |coveralls| image:: https://shields.io/coveralls/github/domdfcoding/cawdrey/master?logo=coveralls
	:target: https://coveralls.io/github/domdfcoding/cawdrey?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/cawdrey?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/cawdrey
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/cawdrey
	:target: https://pypi.org/project/cawdrey/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/cawdrey
	:target: https://pypi.org/project/cawdrey/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/cawdrey
	:target: https://pypi.org/project/cawdrey/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/cawdrey
	:target: https://pypi.org/project/cawdrey/
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/cawdrey?logo=anaconda
	:alt: Conda - Package Version
	:target: https://anaconda.org/domdfcoding/cawdrey

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/cawdrey?label=conda%7Cplatform
	:alt: Conda - Platform
	:target: https://anaconda.org/domdfcoding/cawdrey

.. |license| image:: https://img.shields.io/github/license/domdfcoding/cawdrey
	:alt: License
	:target: https://github.com/domdfcoding/cawdrey/blob/master/LICENSE

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/cawdrey
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/cawdrey/v0.1.5
	:target: https://github.com/domdfcoding/cawdrey/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/cawdrey
	:target: https://github.com/domdfcoding/cawdrey/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. end shields

Installation
----------------

.. start installation

.. tabs::

	.. tab:: from PyPI

		.. prompt:: bash

			pip install cawdrey

	.. tab:: from Anaconda

		First add the required channels

		.. prompt:: bash

			conda config --add channels http://conda.anaconda.org/domdfcoding
			conda config --add channels http://conda.anaconda.org/conda-forge

		Then install

		.. prompt:: bash

			conda install cawdrey

	.. tab:: from GitHub

		.. prompt:: bash

			pip install git+https://github.com//cawdrey@master

.. end installation


.. toctree::
	:hidden:

	Home<self>

.. toctree::
	:maxdepth: 3
	:caption: Documentation

	classes/alphadict
	classes/bdict
	classes/frozendict
	classes/frozenordereddict
	classes/nonelessdict

	base
	Source
	Building

.. start links

View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

`Browse the GitHub Repository <https://github.com/domdfcoding/cawdrey>`__

.. end links