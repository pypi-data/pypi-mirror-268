import gwtc

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "gwtc-tools"
copyright = "2023, Chad Hanna and Others"
author = "Chad Hanna and Others"

fullversion = gwtc.__version__
version = gwtc.__version__


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "numpydoc",
    "sphinx_tabs.tabs",
    "sphinx.ext.mathjax",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "requirements.txt"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "canonical_url": "",
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

numpydoc_show_class_members = False

# Multiversion options
# Whitelist pattern for tags (set to None to ignore all tags)
smv_tag_whitelist = r"^(1.*|0.3.12)$"

# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = r"^master$"

# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = None

# Format for versioned output directories inside the build directory
smv_outputdir_format = "{ref.name}"

# Determines whether remote or local git branches/tags are preferred if their output dirs conflict
smv_prefer_remote_refs = False
