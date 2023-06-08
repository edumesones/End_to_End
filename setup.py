from setuptools import find_packages,setup
from typing import List
def get_librerias(file_path:str)->List[str]:
    '''
    Funcion para obtener librerias necesarias
    '''
    PUNTO_E='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if PUNTO_E in requirements:
            requirements.remove(PUNTO_E)
setup(
    name='proyecto_ML',version='0.0.1',author='edumesones',
    author_email='e.gzlzmesones@gmail.com',
    packages=find_packages(),
    install_requires= get_librerias('requirements.txt')
)