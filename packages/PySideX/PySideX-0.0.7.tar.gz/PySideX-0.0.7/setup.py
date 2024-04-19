from setuptools import setup, find_packages

with open("README.md", "r") as arq:
    readme = arq.read()

with open("LICENSE", "r") as arq:
    licence = arq.read()

setup(
    name="PySideX",
    version="0.0.7",
    license=licence,
    author="Ryan Souza Anselmo",
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email="ryansouza.cwb@email.com",
    keywords="pysidex",
    description="Unofficial PySide6 library, produced with the aim of facilitating the construction of more elegant and improved interfaces using PySide6 technology",
    packages=find_packages(),
    install_requires=["PySide6"],
)
