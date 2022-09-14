import os
import re
from setuptools import find_packages, setup

VERSION = "0.0.1"
DESCRIPTION = "A BASIC PACKAGES THAT CONTAINS TMF 645 MODELS"

setup(
    name='telus_645',
    version=VERSION,
    description=DESCRIPTION,
    url='https://github.com/jose-olmedo-telus/offnet-tmf645-python-types',
    author='José Alejandro Olmedo',
    packages=find_packages(),
    install_requires=[
        'fastapi-camelcase',
        'pydantic'
    ],
    include_package_data=True,
)