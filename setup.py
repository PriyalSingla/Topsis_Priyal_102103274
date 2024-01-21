from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Topsis_Priyal_102103274",
    version="1.0.13",
    author="Priyal Singla",
    author_email="psingla3_be21@thapar.com",
    url="https://github.com/PriyalSingla/Topsis_Priyal_102103274",
    description="A python package for implementing topsis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas", "numpy"],
    entry_points={"console_scripts": ["Topsis_Priyal_102103274 = Topsis_Priyal_102103274.main:main"]},
)