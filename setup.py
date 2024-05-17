# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='dictmeasure',
    version='0.1.0',
    description='count size/length dictionary nodes.',
    long_description='count size/length dictionary nodes.',
    author='yuuki miyoshi',
    author_email='yuuki.miyo@gmail.com',
    url='https://github.com/yuukimiyo/dictmeasure',
    license="MIT",
    keywords="dictionary",
    packages=find_packages(exclude=["src.tests"]),
    package_dir={'': 'src'},
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    tests_require=[],
    test_suite="src.tests",
)