# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pythonEssentials'
copyright = '2022, Henry Cagnini'
author = 'Henry E.L. Cagnini, Thiago C. Naidon'
version = '1.0'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinxcontrib.mermaid']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext'
}

# The master toctree document.
master_doc = 'index'

language = 'pt_BR'

# -- Options for LaTeX output ------------------------------------------------

latex_engine = 'pdflatex'

latex_additional_files = ['mystyle.tex.txt']

latex_elements = {
    'babel': r'\usepackage[brazil]{babel}',
    'inputenc': r'\usepackage[utf8]{inputenc}',
    'releasename': 'Versão',
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '12pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'\input{mystyle.tex.txt}',
    'papersize': 'a4paper'
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (chapters start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'main.tex', 'git Essentials', author.replace(', ', '\\\\'), 'manual'),
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# mermaid_output_format = 'svg'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'nature'

# html_static_path = ['_static']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'github_banner': False,
    'github_user': 'CTISM-Prof-Henry',
    'github_repo': 'gitEssentials',
}

html_sidebars = {
    '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']
}
