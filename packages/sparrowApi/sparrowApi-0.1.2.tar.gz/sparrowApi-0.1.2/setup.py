from setuptools import setup, find_packages

setup(
    name='sparrowApi',
    version='0.1.2',
    description='基于socket的Api工具',
    packages=find_packages(),
    python_requires='>=3.11',
    install_requires=['colorama']
)

