# setup.py

from setuptools import setup, find_packages

setup(
    name='factorial-library',
    version='1.0',
    packages=find_packages(),
    install_requires=[],
    author='Ruban Thirukumaran',
    author_email='rubanthirukumaran@gmail.com',
    description='A simple library to calculate factorial',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Rubanthirukumaran/Cpp-library.git',
    license='MIT',
)
