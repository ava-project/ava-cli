# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('avcli/version.py').read(),
    re.M
    ).group(1)


setup(
    name = "avacli",
    packages = ["avacli"],
    entry_points = {
        "console_scripts": ['avacli = avacli.avacli:main']
    },
    version = version,
    description = "Python command line interface for the AVA Project.",
    author = "Dorian Amouroux",
    author_email = "dor.amouroux@gmail.com",
)
