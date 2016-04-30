try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup


from distutils.extension import Extension

import sys
sys.path.append('../..')
import tools



#download_file='http://www.ipol.im/pub/art/2015/35/classic_edge_detectors_1.0.zip'
#tools.download_and_extract(download_file)  

from pkg_resources import get_build_platform


import numpy as np

sources = ['_wrapper.pyx','../../csources/ace_20121029/ace.c','../../csources/ace_20121029/acecli.c','../../csources/ace_20121029/basic.c','../../csources/ace_20121029/imageio.c']
             
include_dirs=[ np.get_include(),'.']
libraries = []
extra_compile_args=['-std=c99','-lm','-DUSE_LIBPNG']

libraries=[]
library_dirs=[]
if get_build_platform() in ('win32', 'win-amd64'):
	include_dirs+=['../../thirdparties/fftw','../../thirdparties/libpng']
	libraries+=['libfftw3-3','libfftw3f-3','libfftw3l-3']
	libraries+=['libpng12']
	library_dirs+=['../../thirdparties/fftw']
	library_dirs+=['../../thirdparties/libpng']
else:
	extra_compile_args+=['-lfftw3f']
	libraries+=['fftw3f']
	libraries+=['libpng']


if __name__ == '__main__':
	
	extensions = Extension('_wrapper',sources,extra_compile_args=extra_compile_args, libraries=libraries, library_dirs= library_dirs)  
	from Cython.Build import cythonize

	libname="lib"
	setup(
	name = libname,
	ext_modules = cythonize(extensions),  # additional source file(s)),
	include_dirs=include_dirs,
	
	)
