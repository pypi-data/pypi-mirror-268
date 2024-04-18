from setuptools import setup, find_packages

setup(
    name="jr_connection",
    version="0.1",
    description="A simple python package to connect to JR servers and get the data",
    long_description="lalala",
    url="https://github.com/faburry23/JR_Connection",
    author="Felipe Burry",
    author_email="felipe.burry@jriveros.cl",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points={
        "console_scripts": [
            "first_run=jr_connection.first_run:main",
        ],
    },
    classifiers=[
        "Programming Language:: Python:: 3",
        "License:: OSI Approved:: MIT",
        "Operating System:: OS Independent",
    ],
    python_requires=">=3.11",
)
