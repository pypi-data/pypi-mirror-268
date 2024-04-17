import pathlib
from setuptools import setup, find_packages

setup(
    name='FixedSizeFileIOTools',
    version='1.02',
    packages=find_packages(),
    description='Python library for handling fixed sized files, with interactive CLI',
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author='Patryk Jaworski',
    author_email="patrykjaworski9966@gmail.com",
    license='The Unlicense',
    project_urls ={
        "Source": "https://github.com/patrykjawor/FixedSizeFileIOTools"
    },
    install_requires=['pydantic','click'],
    python_requires=">=3.12"
)