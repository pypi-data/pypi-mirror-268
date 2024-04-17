from setuptools import setup, find_packages

setup(
    name='ptcr',
    version='0.1.7',
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
    install_requires=[
        'automata-lib==4.0.0',
        'cached-method==0.1.0',
        'frozendict==2.4.0',
        'mpmath==1.3.0',
        'networkx==3.2.1',
        'numpy==1.26.4',
        'sympy==1.12',
        'scipy==1.13.0',
        'typing-extensions==4.9.0',
        'tqdm==4.66.2',
        'rich==13.7.1'
    ],
    python_requires='==3.9',
    url='https://github.com/T-Lind/ptcr',
    license='MIT',
    keywords='PTCR, FOM, simulation, optimization, decision making, models'
)
