try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup


from distutils.extension import Extension

import sys
sys.path.append('../..')
import tools



download_file='http://www.ipol.im/pub/art/2015/35/classic_edge_detectors_1.0.zip'
tools.download_and_extract(download_file)  



import numpy as np

sources = ['_wrapper.pyx','../../csources/classic_edge_detectors_1.0/classic_edge_detectors.c']
             
include_dirs=[ np.get_include(),'.']

if __name__ == '__main__':
	
	extensions = Extension('_wrapper',sources, extra_compile_args=['-std=c99'])  
	from Cython.Build import cythonize

	libname="lib"
	setup(
	name = libname,
	ext_modules = cythonize(extensions),  # additional source file(s)),
	include_dirs=include_dirs,
	)
