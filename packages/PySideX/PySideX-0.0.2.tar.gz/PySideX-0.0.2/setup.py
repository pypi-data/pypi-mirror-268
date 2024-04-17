from setuptools import setup

with open("PySideX/README.md", "r") as arq:
        readme = arq.read()

with open("PySideX/LICENSE", "r") as arq:
        licence = arq.read()

setup(name='PySideX',
    version='0.0.2',
    license=licence,
    author='Ryan Souza Anselmo',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='ryansouza.cwb@email.com',
    keywords='pysidex',
    description=u'Unofficial PySide6 library, produced with the aim of facilitating the construction of more elegant and improved interfaces using PySide6 technology',
    packages=['PySideX'],
    install_requires=['PySide6'],)