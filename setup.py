from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='jsonjavascriptnotation',
    packages=find_packages(include=['jsonjavascriptnotation']),
    version='0.1.6',
    description='Access JSON using Javascript Object Notation.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Emmerson Miranda',
    license='MIT',
    url='https://github.com/Emmerson-Miranda/jsonjavascriptnotation',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.0'],
    test_suite='tests',
)