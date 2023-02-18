# a setup.py file, which is a Python script that contains information about the project such
# as its name, version, author, and dependencies.

from setuptools import setup,find_packages
from typing import List
# setuptools is a Python library that provides infrastructure for building, distributing, and
# installing Python packages.

# Declaring variables for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.3"
AUTHOR = "Melbin Biju"
DESCRIPTION = "This is my first machine learning project"

REQUIREMENT_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."
# The "-e ." string value for HYPHEN_E_DOT likely represents a command-line option that can
# be passed to the pip package manager, which is used to install and manage Python packages. In particular,
# the "-e" option specifies that the package should be installed in "editable" mode, meaning that any
# changes made to the package's source code will be reflected immediately in the installed package.
# The "." option specifies that the package should be installed in "development mode", which allows
# the package to be installed from the local source tree instead of a built distribution.
# the "local source tree" refers to the directory on your local machine where the package's
# source code is located. This is typically the directory that contains the setup.py file and
# other package files.


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file :
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list :
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)
