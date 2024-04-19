from setuptools import setup, find_packages

setup(
    name="testProject_2",
    version="0.1",
    author="mabrouk",
    author_email="mabrouk@uni-muenster.de",
    description="A simple Python project",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
    ],
)
