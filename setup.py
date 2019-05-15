#!/usr/bin/env python

from setuptools import setup, find_packages
import io

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='catwigopy',
    version='1.0.3',
    description='This tool provides an easy way to generate a preferences profile of a given twitter user',
    packages=find_packages(),
    license='MIT License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Juanju97/Catwigopy',
    author='Juanju',
    author_email='juanjucm17@gmail.com',
    install_requires=['tweepy==3.7.0',
                      'pandas==0.24.2',
                      'numpy==1.16.2'],
    keywords='profile, twitter, natural language processing, NLP, preferences,api',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
