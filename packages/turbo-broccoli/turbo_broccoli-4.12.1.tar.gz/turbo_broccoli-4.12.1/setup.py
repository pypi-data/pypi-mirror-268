#!/usr/bin/env python

"""Setup script"""

import setuptools

name = "turbo_broccoli"
version = "4.12.1"

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().split()

packages = [name] + [
    name + "." + p for p in setuptools.find_packages(where="./" + name)
]

setuptools.setup(
    author="Cédric Ho Thanh",
    author_email="altaris@users.noreply.github.com",
    description="JSON (de)serialization extensions",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    name=name,
    packages=packages,
    platforms="any",
    project_urls={
        "Issues": "https://github.com/altaris/turbo-broccoli/issues",
    },
    python_requires=">=3.10",
    url="https://github.com/altaris/turbo-broccoli",
    version=version,
)
