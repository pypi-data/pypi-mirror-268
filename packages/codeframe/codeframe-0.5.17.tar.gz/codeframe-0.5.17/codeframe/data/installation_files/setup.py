#!/usr/bin/env python3
import os
from setuptools import setup, find_packages

#-----------problematic------
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

import os.path

def readver(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in readver(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name="codeframe",
    description="Automatically created environment for python package",
    author="me",
    url="https://gitlab.com/jaromrax/codeframe",
    author_email="jaromrax@gmail.com",
    license="GPL2",
    version=get_version("codeframe/version.py"),
    packages=['codeframe'],
    package_data={'codeframe': ['data/installation_files/bin_codeframe.py',
                                'data/installation_files/bin/codeframe',
                                'data/installation_files/distcheck.sh',
                                'data/installation_files/codeframe/__init__.py',
                                'data/installation_files/README.org',
                                'data/installation_files/requirements.txt',
                                'data/installation_files/setup.py',
                                'data/installation_files/.bumpversion.cfg',
                                'data/installation_files/.gitignore']},
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    scripts = ['bin/codeframe'],
    install_requires = ['fire','console','sshkeyboard','pytermgui','blessings','terminaltables','pandas','pyfiglet'],
)
