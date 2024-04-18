from setuptools import setup, find_packages

setup(
    name='niels_coloredlogger',
    version='0.2',
    author='Niels',
    packages=find_packages(),
    install_requires=[
        'coloredlogs',
        'logging',
    ]
)
