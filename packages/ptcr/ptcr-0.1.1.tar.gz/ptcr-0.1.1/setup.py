from setuptools import setup, find_packages

setup(
    name='ptcr',
    version='0.1.1',
    author='Tiernan Lindauer',
    author_email='tiernanlind@tamu.edu',
    description='Constructs and simulates PTCR models.',
    long_description=open('README.md').read(),
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='==3.9',
)
