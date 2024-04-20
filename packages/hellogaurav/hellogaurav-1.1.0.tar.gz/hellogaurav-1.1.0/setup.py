#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name='hellogaurav',
    version="1.1.0",
    url='',
    author='graj',
    author_email='graj@cognam.com',
    description=('Test'),
    license='BSD',
    packages=['hellogaurav'],
    # package_dir={'':'src'},
    include_package_data=True,
    install_requires=[],
    zip_safe = False,
)

