import setuptools
from setuptools import setup

setup(
    name='js_code',
    version='1.2.0',
    author="Aduh",
    author_email="aduh73285@gmail.com",
    packages=setuptools.find_packages(),
    description='A small example package',
    install_requires=['PyExecJS2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

