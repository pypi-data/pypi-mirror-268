import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="param-helper",
    version="1.1.1",
    author="EvATive7",
    author_email="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EvATive7/param-helper",
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ),
)