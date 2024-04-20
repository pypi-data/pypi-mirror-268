"""
Setup file for packaging automation
"""

from setuptools import setup, find_packages

VERSION = '2.0.5'
DESCRIPTION = 'A simple calculator app package'
LONG_DESCRIPTION = 'A package that can add or subtract two values'

setup(
    name="hb-calculador-app",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Hjalmar Brand",
    author_email="myemai@mail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='calculator',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
