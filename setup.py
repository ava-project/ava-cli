# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('avacli/version.py').read(),
    re.M
    ).group(1)


setup(
    name="avacli",
    version=version,
    description="Python command line interface for the AVA Project.",
    author="AVA Project",
    author_email="ava_2018@labeip.epitech.eu",
    packages=["avacli"],
    install_requires=[
        'Click',
        'Requests',
    ],
    entry_points={
        "console_scripts": ['avacli = avacli.avacli:cli']
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
