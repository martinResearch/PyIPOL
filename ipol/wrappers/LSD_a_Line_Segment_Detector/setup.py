try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup


from distutils.extension import Extension

import numpy as np

import sys
sys.path.append('..')
import tools



download_file='http://www.ipol.im/pub/art/2012/gjmr-lsd/lsd_1.6.zip'
tools.download_and_extract(download_file)  



sources = ['_wrapper.pyx','../../csources/lsd_1.6/lsd.c']
             
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
