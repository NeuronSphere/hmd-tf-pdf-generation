import pathlib

from setuptools import find_packages, setup

setup(
    name="module_name",
    version="0.0.1",
    description="Example Transform Image to generate a PDF",
    author="Alex Burgoon",
    author_email="alex.burgoon@hmdlabs.io",
    license="unlicensed",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
)
