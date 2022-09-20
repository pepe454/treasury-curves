import setuptools

setuptools.setup(
    name="treasurycurves",
    version="1.0.0",
    author="Danny Fryer",
    author_email="17fryerd@gmail.com",
    description=("query and analyze US Treasury yield data"),
    packages=setuptools.find_packages(),
    py_modules=["treasury"],
    url="https://github.com/pepe454/treasury-curves",
    entry_points={
        "console_scripts": ["treasury=treasury:main"]
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Development Status :: 4 - Beta",
        "License :: MIT License",
    ],
)
