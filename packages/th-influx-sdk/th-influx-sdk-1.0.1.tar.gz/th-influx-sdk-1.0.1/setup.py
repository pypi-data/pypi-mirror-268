# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='th-influx-sdk',
    version='1.0.1',
    description='A SDK for influxDb',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='xiongyi',
    author_email='15679191752@163.com',
    packages=find_packages(),
    install_requires=[
        'influxdb',
        'typing',
        'dateutil==2.9.0',
        'datetime',
        'collections',
        'json'
    ]
)
