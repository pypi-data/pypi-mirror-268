from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))
URL = ""
# Get the long description from the README file
with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="classification_lib",
    version="0.1.0",
    description="Module for libraries containing various utility functions for classification tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    author="Felix Cobby Otoo",
    author_email="felixotoo75@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=["classification_lib"],
    include_package_data=True,
    install_requires=["matplotlib"],
    test_requires=["numpy"],
    test_suite="tests"
)
