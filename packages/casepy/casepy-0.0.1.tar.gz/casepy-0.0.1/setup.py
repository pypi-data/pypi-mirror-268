from setuptools import setup, find_packages

setup(
    name="casepy",
    version="0.0.1",
    description="A Python package for generating cases in a list.",
    url="https://github.com/DongHoon5793/casepy",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    author="DongHoon Kim",
    author_email="donghoon5793@gmail.com",
    packages=find_packages(),
    python_requires=">2.7.0",
    install_requires=[],
)
