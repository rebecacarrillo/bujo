from setuptools import setup, find_packages
import pathlib

# Bujo CLI is just for fun

setup(
    name='bujocli',
    version=0.1,
    description='because we could? CLI with python, Docker, some other stuff',
    author='rebecacarrillo',
    packages=find_packages(where=bujo),
    entry_points={
        'console_scripts': [
            'hey=bujo-cli:main'
        ],
    }
)