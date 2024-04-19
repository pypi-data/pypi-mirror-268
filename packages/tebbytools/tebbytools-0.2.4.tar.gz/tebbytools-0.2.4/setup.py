from setuptools import find_packages, setup

VERSION = "0.2.4"

setup(
    name="tebbytools",
    author="Teddy Gonyea",
    author_email="enterted@gmail.com",
    version=VERSION,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description="A set of simple tools for language learning.",
    long_description="Github: https://github.com/tebby24/tebbytools",
    keywords=["language learning"],
    url="https://github.com/tebby24/tebbytools",
)
