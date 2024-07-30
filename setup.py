from setuptools import  find_packages , setup
from typing import List


def get_requirements(file_path : str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines();
        requirements = [req.replace("\n" , "") for req in requirements]
        return requirements
    
    
setup(
    name="Diamond Price Prediction" ,
    version="0.0.1",
    author="Kush Bajaj",
    author_email="kushbajaj0705@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)