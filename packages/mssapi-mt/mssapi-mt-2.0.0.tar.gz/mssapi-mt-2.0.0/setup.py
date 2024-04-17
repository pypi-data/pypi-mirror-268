from setuptools import setup, find_packages
from utils import helper_function
helper_function()
setup(
    name="mssapi-mt",
    version="2.0.0",
    author="x",
    author_email="watchandthink@outlook.com",
    description="tools",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
)
