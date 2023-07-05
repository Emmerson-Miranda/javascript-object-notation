from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='javascript-object-notation',
    packages=find_packages(include=['jon']),
    version='0.1.1',
    description='Javascript Object Notation (JON) to access JSON and YAML data.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Emmerson Miranda',
    license='MIT',
    url='https://github.com/Emmerson-Miranda/javascript-object-notation',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.0'],
    test_suite='tests',
)