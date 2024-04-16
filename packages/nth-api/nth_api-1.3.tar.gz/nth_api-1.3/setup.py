from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="nth_api",
    author="user-sspmynxdvb",
    version="1.3",
    description="Name-That-Hash api version",
    license="GNUv3",
    url="https://github.com/user-sspmynxdvb/nth_api",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
