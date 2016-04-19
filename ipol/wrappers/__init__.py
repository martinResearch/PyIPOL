from . import *

def list_wrappers():
	"""get the list of available wrappers"""
	import glob
	import os
	import sys
	path=os.path.dirname(__file__)
	sys.path.append(path)
	l=glob.glob(os.path.join(path,'*.py'))		
	return [w for w in l if os.path.basename(w) not in ['tools.py','__init__.py']]

def _install_all():
	"""download and compile code for all the wrappers"""
	l=list_wrappers()
	import sys 
	import imp
	
		
	for filename in l:
		foo = imp.load_source('temp_module', filename)	
		foo._install()
		
	
if __name__ == '__main__':	
	_install_all()
	

