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


# installing each wrapper 
import sys
sys.path.append("./ipol")
from tools import _install_all
_install_all()

import os
paths=['ipol/csources','ipol/examples','ipol/wrappers']
files_to_copy=[]
for path in paths:
	for (dir, _, files) in os.walk(path):
		for f in files:
			files_to_copy.append(os.path.join(dir[len('ipol')+1:], f))
print('found %d file to copy'%len(files_to_copy))


extensions=[]
libname="ipol"
setup(
name = libname,
version= __version_str__,
packages=         ['ipol','ipol.thirdparties','ipol.wrappers'],
ext_modules = cythonize(extensions),  # additional source file(s)),
include_dirs=[ np.get_include(),'./ipol'],
package_data={'ipol':files_to_copy}
)
