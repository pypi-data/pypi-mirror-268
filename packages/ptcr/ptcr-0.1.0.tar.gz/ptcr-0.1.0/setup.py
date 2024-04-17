from setuptools import setup, find_packages
setup(
name='ptcr',
version='0.1.0',
author='Tiernan Lindauer',
author_email='tiernanlind@tamu.edu',
description='Constructs and simulates PTCR models.',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='==3.9',
)