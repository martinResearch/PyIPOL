from . import *
import os
from ..tools import _list_wrappers_paths


		
def run_all_examples():
	
	for filename in _list_wrappers_paths(os.path.dirname(__file__)):
		f=os.path.join(filename,'examples.py')
		print ('running %s...'%f)

		execfile(f,{'__name__' : '__main__'})
		print('done')


		
		
	

