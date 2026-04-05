from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = 'Flipkart-recommender',
    version = '1.9',
    author = 'Me',
    packages = find_packages(),
    install_requires = requirements
)