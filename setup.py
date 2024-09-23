from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement = []
    HYPEN_DOT_E = "-e ."
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n","") for req in requirement]
        if HYPEN_DOT_E in requirement:
            requirement.remove(HYPEN_DOT_E)

    return requirement


setup(
name='mlproject',
version='0.0.1',
author='sudharani vejendla',
author_email='sudharani.vejendla@gmail.com',
packages=find_packages(),
install_requires= get_requirements('requirement.txt')
)