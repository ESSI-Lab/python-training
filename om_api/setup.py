from setuptools import setup, find_packages

setup(
    name="om_api",
    version="0.1.0",
    description="Python client for WHOS API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="ESSI-Lab",
    author_email="email@example.com",
    url="https://github.com/ESSI-Lab/dab-pynb",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "matplotlib",
        "tabulate"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
