from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.34'
DESCRIPTION = 'phenomApis'
LONG_DESCRIPTION = 'A package to access phenom apis'

# Setting up
setup(
    name="phenomApis",
    version=VERSION,
    author="phenom",
    author_email="8297991468h@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['PyJWT==2.4.0', 'certifi==2024.2.2', 'urllib3==1.26.18', 'six==1.16.0'],
    keywords=['resumeparser', 'exsearch'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)