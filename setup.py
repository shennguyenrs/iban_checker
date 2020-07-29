"""
Setup for IBAN Checker
"""

from setuptools import setup, find_packages

setup(
    name="IBAN Checker and Generator",
    version="0.1.0",
    description="A simple script to check IBAN code",
    url="https://github.com/shennguyenrs/iban_checker",
    author="An Nguyen",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 and above",
    ],
    keywords="iban code, script",
    packages=find_packages(include=["iban_checker", "iban_checker.*"]),
)
