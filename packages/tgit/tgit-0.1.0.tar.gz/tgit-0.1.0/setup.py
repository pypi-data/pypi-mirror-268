from setuptools import find_packages, setup

setup(
    name="tgit",
    version="0.1.0",
    packages=find_packages(),
    entry_points={"console_scripts": ["tgit=cli:main"]},
)
