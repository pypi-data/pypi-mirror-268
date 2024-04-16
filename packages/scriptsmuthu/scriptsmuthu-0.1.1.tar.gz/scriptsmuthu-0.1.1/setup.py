from importlib.resources import Package
from pydoc import describe
from setuptools import setup, find_packages

with open("README.md") as f:
    description=f.read()

setup(
    name="scriptsmuthu",
    version="0.1.1",
    packages=find_packages(),
    install_requires=['numpy'],
    
    long_description=description,
    long_description_content_type="text/markdown",
)