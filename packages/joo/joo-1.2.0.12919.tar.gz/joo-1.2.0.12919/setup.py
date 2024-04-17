"""
    This file is part of joo library.
    :copyright: Copyright 1993-2024 Wooloo Studio.  All rights reserved.
    :license: MIT, check LICENSE for details.
"""

import os
from setuptools import setup, find_packages

# get version information
version_filepath = os.path.abspath("./lib/joo/__version__.py")
with open(version_filepath, "r", encoding="utf-8") as f:
    params = {}
    exec(f.read(), None, params)
    version = params.get("__VERSION__")

# get project description
readme_filepath = os.path.abspath("./README.md")
with open(readme_filepath, "r", encoding="utf-8") as f:
    long_description = f.read()

# setup
setup(
    # version information
    name=version["name"],
    description=version["description"],
    version="{}.{}".format(version["version"], version["build"]),
    license=version["license"],
    author=version["author"],
    author_email=version["author_email"],
    url=version["url"],
    project_urls=version["project_urls"],

    # detailed information
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[],

    # package information
    package_dir={"": "lib"},
    packages=find_packages("lib"),
    package_data={"": ["LICENSE"]},
    include_package_data=True,

    # requirements
    platforms="any",
    python_requires="",
    setup_requires=[],
    install_requires=[]
)
