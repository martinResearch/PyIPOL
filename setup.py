try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from distutils.extension import Extension
from Cython.Build import cythonize

import numpy as np

# Get the version number.
import runpy
__version_str__ = runpy.run_path("ipol/version.py")["__version_str__"]

runpy.run_path("ipol/download_ipol.py")

sources = ['ipol/_ipol.pyx','ipol/csources/lsd_1.6/lsd.c','ipol/csources/classic_edge_detectors_1.0/classic_edge_detectors.c']
extensions = Extension('ipol._ipol',sources, extra_compile_args=['-std=c99'])               

libname="ipol"
setup(
name = libname,
version= __version_str__,
ext_modules = cythonize(extensions),  # additional source file(s)),
include_dirs=[ np.get_include(),'./ipol'],
)


