# -*- coding: utf-8 -*-

import os
from setuptools import setup

readmefile = os.path.join(os.path.dirname(__file__), "README.md")
with open(readmefile) as f:
    readme = f.read()

setup(
    name='colab-preamble',
    version="0.1.3",
    description='Prepare google colabpratory by one line of command',
    author='Kota Mori', 
    author_email='kmori05@gmail.com',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/kota7/colab-preamble',
    
    py_modules=['colab_preamble'],
    install_requires=['google-colab', 'another-bigquery-magic']
)
