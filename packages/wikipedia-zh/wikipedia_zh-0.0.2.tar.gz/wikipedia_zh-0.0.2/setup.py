# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name="wikipedia_zh",
    version='0.0.2',
    author="Heng Zhang",
    author_email="1093869292@qq.com",
    description="Wikipedia API for Python",
    url="https://gitee.com/zh19990906/wikipedia_zh",
    install_requires=[
        'beautifulsoup4',
        'requests>=2.0.0,<3.0.0'
    ],
    packages=['code']
)
