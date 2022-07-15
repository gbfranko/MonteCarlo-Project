#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:37:51 2022

@author: gunnarfranko
"""

from setuptools import setup, find_packages


setup(
    name='MonteCarlo',
    version='1.0.0',
    url='https://github.com/gbfranko/MonteCarlo-Project',
    author='Gunnar Franko',
    author_email='gbf6qz@virginia.edu',
    description='Runs a die game',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)
