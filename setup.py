from setuptools import setup,find_packages
from typing import List

#Declare variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Linkan Kumar Sahu"
DESCRIPTION="This is my First END to END ML Project."
PACKAGES=['housing']
REQUIREMENT_FILE_NAME='requirements.txt'

def get_requirements_list()->List[str]: #returns a list of string .  
    """
    Description : This function is going to list of requirements 
    mentioned in requirements.txt file.

    It returns the list which contains name of libraries mentioned in
    requirements.txt file.
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()

)