#!/usr/bin/env python

import shutil
from distutils.core import setup

from setuptools import find_packages


setup(name='RNAformer',
      version='1.0.2',
      packages=find_packages(),
      package_dir={'': '.'},
      dependency_links=[],
      )
