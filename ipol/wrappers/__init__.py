__all__= ['A_Review_of_Classic_Edge_Detectors','Automatic_Color_Enhancement_and_its_Fast_Implementation']

def list_wrappers():
	"""get the list of available wrappers"""
	import glob
	import os
	import sys
	path=os.path.dirname(__file__)
	sys.path.append(path)
	#l=glob.glob(os.path.join(path,'*.py'))		
	#return [w for w in l if os.path.basename(w) not in ['tools.py','__init__.py']]
	return glob.glob(os.path.join(path,'*/'))

def _install_all():
	"""download and compile code for all the wrappers"""
	l=list_wrappers()
	import sys 
	import imp
	import os
		
	for filename in l:
		if os.path.isfile(os.path.join(filename,'setup.py')):#cython binding
			os.system('cd %s;python setup.py build_ext --inplace'%filename)
		else:	
			filew=os.path.join(filename,'install.py')
			if not os.path.isfile(filew):
				raise Exception('file %s not found'%filew)
				
			foo = imp.load_source('temp_module',filew)	
			foo._install()	
		
		
		
		
	
if __name__ == '__main__':	
	_install_all()
	

