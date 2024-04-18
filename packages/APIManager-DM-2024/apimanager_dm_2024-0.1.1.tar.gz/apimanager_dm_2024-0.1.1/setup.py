from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="APIManager-DM-2024",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        'requests>=2.31.0'
    ],
    url="https://github.com/movsdav/APIManager_DM_2024",
    long_description_content_type="text/markdown",
    long_description=description
)
