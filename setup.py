from distutils.core import setup,Extension
from Cython.Build import cythonize
import numpy as np

sources = ['ipol.pyx','csources/lsd_1.6/lsd.c','csources/classic_edge_detectors_1.0/classic_edge_detectors.c']
extensions = Extension('ipol',sources, extra_compile_args=['-std=c99'])               

libname="ipol"
setup(
name = libname,
ext_modules = cythonize(extensions),  # additional source file(s)),
include_dirs=[ np.get_include()],
)


