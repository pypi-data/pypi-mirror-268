from setuptools import find_packages, setup

VERSION = "0.1.4"

setup(
    name="langbank",
    author="Teddy Gonyea",
    author_email="enterted@gmail.com",
    version=VERSION,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description="A simple word bank for language learning",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords=["language learning"],
    url="https://github.com/tebby24/langbank",
)
