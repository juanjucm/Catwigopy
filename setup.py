#!/usr/bin/env python

from setuptools import setup, find_packages
import io

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='catwigopy',
    version='1.0.2',
    description='This tool provides an easy way to generate a preferences profile of a given twitter user',
    packages=find_packages(),
    license='MIT License',
    long_description=long_description,
    url='https://github.com/Juanju97/TwitterPreferencesProfile',
    author='Juanju',
    author_email='juanjucm17@gmail.com',
    install_requires=['tweepy==3.7.0', 'xlrd==1.2.0'],
    keywords='profile, twitter, natural language processing, NLP, preferences,api',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
