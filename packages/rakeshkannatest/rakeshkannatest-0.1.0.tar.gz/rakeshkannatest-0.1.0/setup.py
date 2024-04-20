
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rakeshkannatest",
    version="0.1.0",
    description="My first module",
    author="Rakesh Kanna",
    author_email='rakeshkanna0108@gmail.com',
    licence="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=['first', 'module', 'python'],
)
