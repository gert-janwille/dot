#!/usr/bin/env python
"""
This module tries to install all the required software.
"""
import os
from setuptools import setup, find_packages

NAME = "Dot"
AUTHOR = "gert-janwille"
URL = "https://github.com/gert-janwille/dot"
DESCRIPTION = "Automated lightweight project who will do everything"
LICENSE = "MIT"
KEYWORDS = ["dot", "evil"]
PACKAGES = find_packages(exclude=["docs", "tests"])
INCLUDE_PACKAGE_DATA = True
VERSION = "0.0.1"
CLASSIFIERS = ["Development Status :: 1 - Planning",
               "Natural Language :: English", "Operating System :: Unix",
               "Programming Language :: Python :: 2", "Programming Language :: Python :: 2.7",
               "Programming Language :: Python :: 2 :: Only", "Topic :: Security",
               "Topic :: System :: Networking", "Intended Audience :: End Users/Desktop",
               "Intended Audience :: System Administrators",
               "Intended Audience :: Information Technology"]
ENTRY_POINTS = {"console_scripts": ["dot = dot.pydot:run"]}

INSTALL_REQUIRES = ["pexpect", "future", "youtube_dl"]

# run setup
setup(name=NAME, author=AUTHOR, description=DESCRIPTION,
      license=LICENSE, keywords=KEYWORDS, packages=PACKAGES,
      include_package_data=INCLUDE_PACKAGE_DATA, version=VERSION, entry_points=ENTRY_POINTS,
      install_requires=INSTALL_REQUIRES, classifiers=CLASSIFIERS, url=URL)


print("                    |_   _ `.  .'   `. |  _   _  |              ")
print("                      | | `. \/  .-.  \|_/ | | \_|            ")
print("                      | |  | || |   | |    | |                ")
print(r"                     _| |_.' /\  `-'  /   _| |_                ")
print(r"                    |______.'  `.___.'   |_____|              ")
print("                                                               ")
