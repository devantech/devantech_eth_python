from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='devantech_eth',
    packages=find_packages(include=['devantech_eth']),
    version='0.1.0',
    long_description = long_description,
    long_description_content_type="text/markdown",
    description='Python library for controlling Devantech ETH modules.',
    author='James Henderson',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
