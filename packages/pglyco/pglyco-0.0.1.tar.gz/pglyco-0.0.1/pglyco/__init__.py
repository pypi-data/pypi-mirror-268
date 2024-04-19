#!python

import warnings
warnings.filterwarnings("ignore")

__project__ = "pglyco"
__version__ = "0.0.1"
__license__ = "Apache"
__description__ = "An open-source Python package of pGlyco."
__author__ = "Mann Labs"
__author_email__ = "jalew.zwf@qq.com"
__github__ = "https://github.com/FennOmix/pGlyco"
__keywords__ = [
    "bioinformatics",
    "glycoproteomics",
    "mass spectrometry",
    "search engine",
]
__python_version__ = ">=3.8"
__classifiers__ = [
    "Development Status :: 1 - Planning",
    # "Development Status :: 2 - Pre-Alpha",
    # "Development Status :: 3 - Alpha",
    # "Development Status :: 4 - Beta",
    # "Development Status :: 5 - Production/Stable",
    # "Development Status :: 6 - Mature",
    # "Development Status :: 7 - Inactive"
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
]
__urls__ = {
    "GitHub": __github__,
    # "ReadTheDocs": None,
    # "PyPi": None,
    # "Scientific paper": None,
}
__console_scripts__ = [
    "pglyco=pglyco.cli:run",
]
