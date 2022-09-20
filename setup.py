import setuptools

setuptools.setup(
    name="treasurycurves",
    version="1.0.0",
    author="Danny Fryer",
    author_email="17fryerd@gmail.com",
    description=("query and analyze US Treasury yield data"),
    packages=setuptools.find_packages(),
    url="https://github.com/pepe454/treasury-curves",
    entry_points={
        "console_scripts": ["treasury-curves=treasurycurves.treasury.__main__"]
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Development Status :: 4 - Beta",
        "License :: MIT License",
    ],
)
