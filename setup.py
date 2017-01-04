#!/usr/bin/env python
from distutils.core import setup


setup(
    name='invoice_db',
    version='1.0',
    description='',
    author='Maya Brandi',
    author_email='maya.brandi@scilifelab.se',
    packages=['clinicaladmin'],
    install_requires=[
        'Flask',
        'Flask-Admin',
        'ruamel.yaml',
        'click',
        'Flask-SQLAlchemy',
        'six',
    ],
    entry_points={
        'console_scripts': ['admin = clinicaladmin.cli:root'],
    },
)
