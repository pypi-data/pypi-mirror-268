# -*- coding: utf-8 -*-
import setuptools
from setuptools import find_packages

setuptools.setup(
    name="wikipedia_zh",
    version='0.0.5',
    author="Heng Zhang",
    author_email="1093869292@qq.com",
    description="Wikipedia Zh API for Python",
    url="https://gitee.com/zh19990906/wikipedia_zh",
    install_requires=[
        'beautifulsoup4',
        'requests>=2.0.0,<3.0.0'
    ],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)


