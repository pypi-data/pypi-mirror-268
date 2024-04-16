# -*- coding: utf-8 -*-
import setuptools
from setuptools import find_packages

setuptools.setup(
    name="wikipedia-zh",
    version='0.0.1',
    author="Heng Zhang",
    author_email="1093869292@qq.com",
    description="Wikipedia API for Python",
    license="MIT",
    keywords="python wikipedia-zh API",
    url="https://gitee.com/zh19990906/wikipedia_zh",
    install_requires=[
        'beautifulsoup4',
        'requests>=2.0.0,<3.0.0'
    ],
    packages=find_packages()
)
