from setuptools import setup, find_packages

setup(
    name="shapecomp",
    version="0.5.0b0",
    packages=find_packages(),
    install_requires=[
        "pythonnet"
    ],
    author="Peter Grønbæk Andersen",
    author_email="peter@grnbk.io",
    description="A module for compressing and decompressing shape files, powered by the TK.MSTS.Tokens.dll library from Okrasa Ghia.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pgroenbaek/shapecomp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)