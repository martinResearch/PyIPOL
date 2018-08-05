# this script will download the original C++ codes from  IPOL and eventually patch some of the code

import os
import zipfile
import tarfile
from PIL import Image
import numpy as np
import subprocess
import sys

if sys.version_info[0] == 2:
    from urllib import urlretrieve
else:
    from urllib.request import urlretrieve

path=os.path.dirname(__file__)
extraction_directory=os.path.join(path,'csources')


def download_and_extract(f,subfolder=''):	
	print("downloading %s..."%f,end='')
	local_filename, headers = urlretrieve(f)
	print("done")
	print("decompressing the zip file %s..."%local_filename ,end='')
	if not os.path.isdir(extraction_directory):
		os.mkdir(extraction_directory)
	if f[-3:]=='zip':
		with zipfile.ZipFile(local_filename) as zf:
			zf.extractall(extraction_directory+subfolder)
	elif f[-2:]=='gz':
		with tarfile.open(local_filename, "r") as tar:
			tar.extractall(extraction_directory+subfolder)
	else:
		print('unrecognized archive type')
		raise
	print("done")
	
	
def read_animated_gif(file):
	im = Image.open(file)
	i= 0
	images=[]
	while 1:
		try:
			im.seek(i)
		except:
			break
		imframe = im.copy()
		if i == 0: 
			palette = imframe.getpalette()
		else:
			imframe.putpalette(palette)
		palettenp=255-np.array(palette).reshape(-1,3)
		images.append(palettenp[np.array(imframe)])
		i += 1
	return images


import os

import imp

wrappers_path=os.path.join(os.path.dirname(__file__),'wrappers')

def _list_wrappers(path=None):
	if path is None:
		path=wrappers_path
	d=path
	return [o for o in os.listdir(d) if os.path.isdir(os.path.join(d,o)) and o!='new_paper_example']

__all__= _list_wrappers()

def _list_wrappers_paths(path=None):
	"""get the list of available wrappers"""
	print(path)
	import glob
	import os
	import sys
	if path is None:
		path=wrappers_path

	return [os.path.join(path,p) for p in _list_wrappers(path)]
	
	
def _install(filename):
		print('installing %s'%filename)
		if os.path.isfile(os.path.join(filename,'setup.py')):#cython binding
			pass
			subprocess.call('python setup.py build_ext --inplace',shell=True,cwd=filename)
			#os.system('cd %s;python setup.py build_ext --inplace'%filename)
			#execfile(' %s/setup.py '%filename,[build_ext --inplace])
		else:	
			filew=os.path.join(filename,'install.py')
			if not os.path.isfile(filew):
				raise Exception('file %s not found'%filew)
				
			foo = imp.load_source('temp_module',filew)	
			foo._install()	

def _install_all(path=None):
	"""download and compile code for all the wrappers"""
	print('------------------------------------------------')
	print(' download and compile code for all the wrappers')
	l=_list_wrappers_paths(path)
	import sys 
	import imp
	import os
	for filename in l:
		_install(filename)
		


