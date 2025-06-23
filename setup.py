from setuptools import find_packages,setup
from typing import List

def get_requiremnts(file_path:str)->List[str]:
    '''
    THIS FUNTION WILL RETURN THE LIST OF REQUIREMNTS
    '''
    requiretments=[]
    with open(file_path) as file_obj:
        requiretments=file_obj.readlines()
        requiretments=[req.replace('\n',"") for req in requiretments]
    return requiretments


setup(
name='mlporject',
version='0.0.1',
author='Rahul Krishna',
author_email='vs.rahulkrishna@outlook.com',
packages=find_packages(),
install_requires=get_requiremnts('requirement.txt')
)