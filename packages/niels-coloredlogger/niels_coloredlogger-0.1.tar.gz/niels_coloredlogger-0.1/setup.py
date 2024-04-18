from setuptools import setup, find_packages

setup(
    name='niels_coloredlogger',
    version='0.1',
    author='Niels',
    packages=find_packages(),
    install_requires=[
        'coloredlogs',
        'logging',
    ]
)
