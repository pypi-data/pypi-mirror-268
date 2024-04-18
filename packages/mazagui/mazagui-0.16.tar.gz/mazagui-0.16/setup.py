#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages
import pip



version='0.16'
libName="mazagui"


with open("README.md", "r") as fh:
	long_description = fh.read()
short_description = "GUI for cross-platform 2d/3d image segmentation C++ library"

installRequiresList=['mazalib','matplotlib','tk','Pillow','imageio']

pip.main(['install'] + installRequiresList)

setup(
	name=libName,
	version=version,
	description=short_description,
	long_description=long_description,
	long_description_content_type="text/markdown",
	author='Mathieu Gravey, Roman V. Vasilyev, Timofey Sizonenko, Kirill M. Gerke, Marina V. Karsanina, Andrey A. Ananev',
	author_email='mathieu.gravey@unil.ch',
	license='GPLv3',
	packages=find_packages('src',include=['mazagui']),
	package_dir={'': 'src'},
	package_data={'mazagui': ['./MAZAlib.ico']},
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Science/Research',
		'Intended Audience :: Education',
		'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
		'Programming Language :: C++',
		'Programming Language :: Python :: 3 :: Only',
		'Operating System :: OS Independent'
	],
	install_requires=installRequiresList
)
