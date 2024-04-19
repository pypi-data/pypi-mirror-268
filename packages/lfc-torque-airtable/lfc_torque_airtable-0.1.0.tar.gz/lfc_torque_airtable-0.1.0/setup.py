#!/usr/bin/env python

from distutils.core import setup

main_ns = {}
with open("lfc_torque_airtable/version.py") as ver_file:
    exec(ver_file.read(), main_ns)

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="lfc-torque-airtable",
    version=main_ns["__version__"],
    description="Torque airtable connection for LFC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Open Tech Strategies, LLC",
    author_email="frankduncan@opentechstrategies.com",  # For now, this works
    url="https://code.librehq.com/ots/mediawiki/lfc-torque-airtable",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["lfc-torque-airtable=lfc_torque_airtable.main:main"],
    },
    packages=[
        "lfc_torque_airtable",
    ],
    install_requires=[
        "torqueclient",
        "pyairtable",
    ],
    package_dir={"": "."},
    python_requres=">=3.10",
)
