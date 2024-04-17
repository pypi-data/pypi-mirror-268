from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

setup(
    name='pyMetaheuristic',
    version='1.9.5',
    license='GNU',
    author='Valdecy Pereira',
    author_email='valdecy.pereira@gmail.com',
    url='https://github.com/Valdecy/pyMetaheuristic',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'plotly',
        'scipy'
    ],
    description='pyMetaheuristic: A Comprehensive Python Library for Optimization',
    long_description=long_description,
    long_description_content_type='text/markdown',
)