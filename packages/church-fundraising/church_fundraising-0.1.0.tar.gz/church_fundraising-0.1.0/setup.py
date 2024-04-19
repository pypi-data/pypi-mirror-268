# setup.py

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="church-fundraising",
    version="0.1.0",
    author="Ruban Thirukumaran",
    author_email="rubanthirukumaran@gmail.com",
    description="A library for managing products and transactions for church fundraising",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rubanthirukumaran/Cpp-library.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
