#!/usr/bin/env python

import os.path

from setuptools import setup, find_packages
import selenium_page as sp

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requires = ['selenium >= 2.28']

setup(
    name='selenium-page',
    version=sp.__version__,
    author=sp.__author__,
    author_email=sp.__email__,
    maintainer=sp.__maintainer__,
    maintainer_email=sp.__email__,
    url=sp.__url__,
    download_url=sp.__url__,

    description=sp.__summary__,
    long_description = read('README.md'),

    license=sp.__license__,
    packages=find_packages(),

    install_requires=requires,

    test_suite="tests.suite",

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.4'],
    zip_safe = True)
