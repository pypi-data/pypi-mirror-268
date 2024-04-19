#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

package_dir = {
    'paper2vec': 'paper2vec',
    'paper2vec.datadestination': 'paper2vec/datadestination',
    'paper2vec.datasource': 'paper2vec/datasource',
    'paper2vec.vectorizer': 'paper2vec/vectorizer',
    'paper2vec.scripts': 'paper2vec/scripts',
}

setup(
    name='paper2vec',
    version='0.2',
    author='yindaheng98',
    author_email='yindaheng98@gmail.com',
    url='https://github.com/yindaheng98/paper2vec',
    description=u'Turn your collected papers into vectors!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir=package_dir,
    packages=[key for key in package_dir],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'neo4j>=5.15.0',
        'openai>=1.21.2',
        'qdrant-client>=1.8.2'
    ],
)
