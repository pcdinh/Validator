#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'Validator',
    version = '0.0.1',
    description = 'A python module used for setting up validation rules.',
    author = 'Wilhelm Murdoch',
    author_email = 'wilhelm.murdoch@gmail.com',
    url = 'http://www.thedrunkenepic.com/',
    packages = ['validator']
)