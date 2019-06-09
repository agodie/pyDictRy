import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyDictRy-agodie",
    version="0.0.1",
    author="agodie",
    author_email="agodie.developer@gmail.com",
    description="Query facilities for ordinary dictionaries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/agodie/pyDictRy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
)
