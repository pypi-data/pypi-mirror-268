from setuptools import setup, find_packages
import codecs
import os
VERSION = '0.0.2'
DESCRIPTION = 'A powerpacked visualisation of Algorithms'
LONG_DESCRIPTION = 'A package that allows to understand user about algorithms.'

# Setting up
setup(
    name="pyalgobox",
    version=VERSION,
    author="Tanay Prabhakar (@tanayprabhakar)",
    author_email="<tanayprabhakar10@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['matplotlib','numpy'],
    keywords=['python', 'algorithm', 'data visualisation', 'college project'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)