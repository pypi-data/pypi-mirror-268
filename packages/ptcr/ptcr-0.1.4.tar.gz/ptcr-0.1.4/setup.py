from setuptools import setup, find_packages

setup(
    name='ptcr',
    version='0.1.4',
    author='Tiernan Lindauer',
    author_email='tiernanlind@tamu.edu',
    description='Constructs and simulates PTCR models.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='==3.9',
    url='https://github.com/T-Lind/ptcr',
    license='MIT',
    keywords='PTCR, FOM, simulation, optimization, decision making, models'
)
