#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from glob import glob
from os import path, environ
from setuptools import setup, find_packages

# Include extensions only when not on readthedocs.org
if environ.get('READTHEDOCS', None) == 'True':
    extensions = []
else:
    from numpy.distutils.core import setup, Extension
    extensions = [
        Extension(name='apexpy.fortranapex',
                  sources=['fortranapex/magfld.f', 'fortranapex/apex.f',
                           'fortranapex/makeapexsh.f90',
                           'fortranapex/igrf.f90',
                           'fortranapex/apexsh.f90',
                           'fortranapex/checkapexsh.f90',
                           'apexpy/fortranapex.pyf'])]

setup_kwargs = {'ext_modules': extensions, 'packages': find_packages()}

setup(**setup_kwargs)
