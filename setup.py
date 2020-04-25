#!/usr/bin/env python
"""Setup script"""

from __pkginfo__ import (
	author, author_email, install_requires,
	license, long_description, classifiers,
	modname, short_desc, VERSION, web,
	project_urls, keywords,
	)

from setuptools import setup, find_packages

setup(
		author=author,
		author_email=author_email,
		classifiers=classifiers,
		description=short_desc,
		entry_points=None,
		install_requires=install_requires,
		license=license,
		long_description=long_description,
		name=modname,
		packages=find_packages(exclude=("tests",)),
		py_modules=None,
		url=web,
		project_urls=project_urls,
		version=VERSION,
		python_requires=">=3.6",
		keywords=keywords,
		)
