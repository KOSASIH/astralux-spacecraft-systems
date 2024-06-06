from setuptools import setup, find_packages

setup(
    name='carfield',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['numpy', 'pandas', 'cikit-learn'],
    author='Astralux Spacecraft Systems',
    author_email='[astralux@spacecraft.systems](mailto:astralux@spacecraft.systems)'
)
