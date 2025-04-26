from setuptools import setup, find_packages

# fetch all the required files mention the requirement.txt file 

def get_requirements():
    with open('requirement.txt') as f:
        requirements = f.read().splitlines()
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name='ML_project',
    version='0.1.0',
    description='A machine learning project',
    author='Mandal',
    author_email='chanchalmandal146@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements()
)

