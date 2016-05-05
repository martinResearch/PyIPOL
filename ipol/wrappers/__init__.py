from . import *

from ..tools import _list_wrappers_paths
import os

		
def run_all_examples():
	
	for filename in _list_wrappers_paths():
		f=os.path.join(filename,'examples.py')
		print('running %s...'%f)

		execfile(f,{'__name__' : '__main__'})
		print('done')


		
		
	

