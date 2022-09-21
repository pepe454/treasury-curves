import os
import sys

# root directory
sys.path.insert(0, os.path.abspath("../"))


# -- Project information -----------------------------------------------------

project = 'treasurycurves'
copyright = '2022, Danny Fryer'
author = 'Danny Fryer'
version = 'v1.0.2'
release = version

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "m2r2",
]
templates_path = ['_templates']
exclude_patterns = ["../README.md", "../setup.py", "../test_treasury.py"]
source_suffix = [".rst"]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
