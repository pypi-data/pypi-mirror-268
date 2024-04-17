from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="unstract-dropboxdrivefs",
    version="1.0.1",
    packages=["dropboxdrivefs"],
    install_requires=["fsspec", "requests", "dropbox"],
    author="Zipstack Inc",
    author_email="devsupport@zipstack.com",
    url = "https://github.com/Zipstack/dropboxdrivefs/",
    description="Dropbox implementation by Unstract for fsspec module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.5",
    license="BSD",
    zip_safe=False,
)
