#!/usr/bin/env python

"""The setup script."""


import os

import rtsstat as module
from setuptools import find_packages, setup


def walker(base, *paths):
    file_list = set([])
    cur_dir = os.path.abspath(os.curdir)

    os.chdir(base)
    try:
        for path in paths:
            for dname, dirs, files in os.walk(path):
                for f in files:
                    file_list.add(os.path.join(dname, f))
    finally:
        os.chdir(cur_dir)

    return list(file_list)


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup_requirements = 'pytest-runner'

test_requirements = 'pytest'

setup(
    author="Julian Wanner",
    author_email='jwgithub@mailbox.org',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="rtsstat. A mlf-core based .",
    entry_points={
        'console_scripts': [
            'rtsstat=rtsstat.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='rtsstat',
    name='rtsstat',
    packages=find_packages(include=['rtsstat', 'rtsstat.*']),
    package_data={
        module.__name__: walker(
            os.path.dirname(module.__file__),
            'data'
        ),
    },
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    url='https://github.com/waseju/rtsstat',
    version='0.1.5',
    zip_safe=False,
)
