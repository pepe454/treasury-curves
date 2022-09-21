import setuptools

setuptools.setup(
    name="treasurycurves",
    version="1.0.0",
    author="Danny Fryer",
    author_email="17fryerd@gmail.com",
    description=("query and analyze US Treasury yield data"),
    packages=setuptools.find_packages(),
    py_modules=["treasury"],
    license="MIT",
    url="https://github.com/pepe454/treasury-curves",
    keywords="treasury",
    entry_points={
        "console_scripts": ["treasury=treasury:main"]
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Development Status :: 4 - Beta",
        "License :: MIT License",
    ],
    install_requires=[
        "pandas",
        "requests",
        "matplotlib"
    ],
)
