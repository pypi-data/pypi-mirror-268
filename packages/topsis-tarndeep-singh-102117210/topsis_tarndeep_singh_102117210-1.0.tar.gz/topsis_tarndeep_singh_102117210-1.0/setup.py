from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0'
DESCRIPTION = 'topsis_tarndeep_singh_102117210'
LONG_DESCRIPTION = 'A multi-criteria decision-making method used to determine the best choice among a set of alternatives'

# Setting up
setup(
    name="topsis_tarndeep_singh_102117210",
    version=VERSION,
    author="TARNDEEP SINGH",
    author_email="<tsingh3_be21@thapar.edu>",
    description='A package for performing TOPSIS analysis',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['python', 'numpy', 'pandas', 'sys'],
    keywords=['python', 'topsis'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
