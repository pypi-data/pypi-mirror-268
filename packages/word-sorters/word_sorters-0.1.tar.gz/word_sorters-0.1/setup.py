# setup.py
from setuptools import setup, find_packages

setup(
    name='word_sorters',
    version='0.1',
    packages=find_packages(),
    description='A simple library to sort words alphabetically',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='chinmay',
    author_email='lawd7131@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)