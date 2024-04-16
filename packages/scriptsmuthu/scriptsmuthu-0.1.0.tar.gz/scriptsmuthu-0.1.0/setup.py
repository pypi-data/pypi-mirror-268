from importlib.resources import Package
from setuptools import setup, find_packages

setup(
    name="scriptsmuthu",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy'
    ],
)