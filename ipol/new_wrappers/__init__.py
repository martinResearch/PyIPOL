import os
from . import *
import imp

def _list_wrappers():
	d=os.path.dirname(__file__)
	return [o for o in os.listdir(d) if os.path.isdir(os.path.join(d,o)) and o!='new_paper_example']

__all__= _list_wrappers()


def _list_wrappers_paths():
	"""get the list of available wrappers"""
	import glob
	import os
	import sys
	path=os.path.dirname(__file__)
	return [os.path.join(path,p) for p in _list_wrappers()]
	
	
def _install(filename):
	
		if os.path.isfile(os.path.join(filename,'setup.py')):#cython binding
			os.system('cd %s;python setup.py build_ext --inplace'%filename)
			#execfile(' %s/setup.py '%filename,[build_ext --inplace])
		else:	
			filew=os.path.join(filename,'install.py')
			if not os.path.isfile(filew):
				raise Exception('file %s not found'%filew)
				
			foo = imp.load_source('temp_module',filew)	
			foo._install()	

def _install_all():
	"""download and compile code for all the wrappers"""
	l=_list_wrappers_paths()
	import sys 
	import imp
	import os
	for filename in l:
		_install(filename)
		

		
def run_all_examples():
	
	for filename in _list_wrappers_paths():
		f=os.path.join(filename,'examples.py')
		print 'running %s...'%f
		execfile(f,{'__name__' : '__main__'})
		print 'done'


		
		
	
if __name__ == '__main__':	
	_install_all()
	

