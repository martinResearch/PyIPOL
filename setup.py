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

import download_ipol

sources = ['ipol/_ipol.pyx','ipol/csources/lsd_1.6/lsd.c','ipol/csources/classic_edge_detectors_1.0/classic_edge_detectors.c']
extensions = Extension('ipol._ipol',sources, extra_compile_args=['-std=c99'])               

libname="ipol"
setup(
name = libname,
version= __version_str__,
packages=         ['ipol','ipol.thirdparties'],
ext_modules = cythonize(extensions),  # additional source file(s)),
include_dirs=[ np.get_include(),'./ipol'],
include_package_data = True,
package_data = {'ipol':['*.txt', '*.rst','*.png','*.jpg','*.bmp','csources/lsd_1.6/*.pgm']},
)

#from distutils import sysconfig
#from distutils import dir_util
#import os
#destination_path = sysconfig.get_python_lib()
#package_path = os.path.join(destination_path, libname,'csource2')
#print 'copying c source code and data to %s'%package_path
#dir_util.copy_tree('ipol/csources', package_path, update=1, preserve_mode=0)

