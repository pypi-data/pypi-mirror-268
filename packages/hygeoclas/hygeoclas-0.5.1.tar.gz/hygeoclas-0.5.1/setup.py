from setuptools import setup, find_packages

setup(
    name="hygeoclas",
    version="0.5.1",
    description="Package for hydrogeological classifcation",
    author="Brayan A. Quiceno",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "numpy",
        "pandas",
        "seaborn",
        "torch"
    ],
)