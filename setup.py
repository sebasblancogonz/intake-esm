#!/usr/bin/env python

"""The setup script."""

from os.path import exists

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')


if exists('README.rst'):
    with open('README.rst') as f:
        long_description = f.read()
else:
    long_description = ''

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Scientific/Engineering',
]

setup(
    name='intake-esm',
    description='An intake plugin for building and loading earth system data sets such as CMIP, CESM Large Ensemble',
    long_description=long_description,
    python_requires='>=3.6',
    maintainer='Anderson Banihirwe',
    maintainer_email='abanihi@ucar.edu',
    classifiers=CLASSIFIERS,
    url='https://github.com/NCAR/intake-esm',
    packages=find_packages(exclude=('tests',)),
    package_dir={'intake-esm': 'intake-esm'},
    include_package_data=True,
    install_requires=install_requires,
    license='Apache 2.0',
    zip_safe=False,
    entry_points={'intake.drivers': ['esm_datastore = intake_esm.core:esm_datastore']},
    keywords='intake-esm',
    use_scm_version={'version_scheme': 'post-release', 'local_scheme': 'dirty-tag'},
    setup_requires=['setuptools_scm', 'setuptools>=30.3.0'],
)
