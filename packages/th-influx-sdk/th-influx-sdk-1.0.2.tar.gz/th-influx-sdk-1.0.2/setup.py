# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='th-influx-sdk',
    version='1.0.2',
    description='A SDK for influxDb',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='xiongyi',
    author_email='15679191752@163.com',
    packages=find_packages(),
    install_requires=[
        'influxdb==5.3.2',  # 替换为你需要的influxdb版本
        'python-dateutil>=2.9.0.post0',  # dateutil通常作为python-dateutil包分发
    ]
)
