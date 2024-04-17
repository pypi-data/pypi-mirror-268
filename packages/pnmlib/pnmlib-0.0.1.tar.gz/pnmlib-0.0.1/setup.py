import os
import sys
import os.path
from distutils.util import convert_path
from setuptools import setup, find_packages

sys.path.append(os.getcwd())
ver_path = convert_path('openpnm/__version__.py')


setup(
    name='pnmlib',
    description='A library of pore netwwork modeling functions',
    version='0.0.1',
    classifiers=[
    ],
    packages=find_packages("."),
    install_requires=[
        'h5py',
        'matplotlib',
        'networkx',
        'numba',
        'numpy',
        'pandas',
        'pyamg',
        'pypardiso',
        'rich',
        'scipy',
        'sympy',
        'tqdm',
        'transforms3d',
    ],
    author='PMEAL Team',
    author_email='jgostick@uwaterloo.ca',
    download_url='https://www.pmeal.com/',
    url='http://pmeal.com',
    project_urls={
    },
)
