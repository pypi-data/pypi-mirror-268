# setup.py

from setuptools import setup, find_packages

setup(
    name='news-app-api',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Vaishnavi Deshpande',
    author_email='x23183209@student.ncirl.ie',
    description='A Python library for interacting with the News API',
    url='https://github.com/dvaishnavi8631/dvaish_private.git',
)
