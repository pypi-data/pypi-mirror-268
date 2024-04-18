from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="APIManager-DM-2024",
    version="0.0.10",
    packages=find_packages(),
    install_requires=[
        'requests>=2.31.0'
    ],
    long_description=description,
    long_description_content_type="text/markdown"
)
