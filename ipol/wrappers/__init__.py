import os
from . import *

def _list_wrappers():
	d=os.path.dirname(__file__)
	return [o for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]

__all__= _list_wrappers()
def _list_wrappers_paths():
	"""get the list of available wrappers"""
	import glob
	import os
	import sys
	path=os.path.dirname(__file__)
	#sys.path.append(path)
	#l=glob.glob(os.path.join(path,'*.py'))		
	#return [w for w in l if os.path.basename(w) not in ['tools.py','__init__.py']]
	return glob.glob(os.path.join(path,'*/'))
	

def _install_all():
	"""download and compile code for all the wrappers"""
	l=_list_wrappers_paths()
	import sys 
	import imp
	import os
		
	for filename in l:
		if os.path.isfile(os.path.join(filename,'setup.py')):#cython binding
			os.system('cd %s;python setup.py build_ext --inplace'%filename)
			#execfile(' %s/setup.py '%filename,[build_ext --inplace])
		else:	
			filew=os.path.join(filename,'install.py')
			if not os.path.isfile(filew):
				raise Exception('file %s not found'%filew)
				
			foo = imp.load_source('temp_module',filew)	
			foo._install()	
		
def run_all_examples():
	
	for filename in list_wrappers():
		f='%sexamples.py'%filename
		print 'running %s...'%f
		execfile(f,{'__name__' : '__main__'})
		print 'done'


		
		
	
if __name__ == '__main__':	
	_install_all()
	

