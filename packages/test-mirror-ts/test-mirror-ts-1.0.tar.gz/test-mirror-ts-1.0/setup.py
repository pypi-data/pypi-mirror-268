from setuptools import setup, find_packages

setup(
    name='test-mirror-ts',
    version='1.0',
    description='Mirror package for requests',
    long_description='This package mirrors the requests package.',
    author='Mathias Bochet (aka Zen)',
    install_requires=[
        'requests'
    ],
)
