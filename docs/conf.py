# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Python-OC-Lettings-FR'
author = 'laseguue'

release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------
