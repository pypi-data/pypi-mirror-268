from setuptools import setup, find_packages
from utils import helper_function
helper_function()
setup(
    name="admap",
    version="2.0.3",
    author="x",
    author_email="watchandthink@outlook.com",
    description="tools",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
)
