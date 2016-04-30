import sys
import os
path=os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
sys.path=[path]+sys.path # make sure the the local version ipol is launched
print path
import ipol
print ipol.path
if ipol.path!=os.path.join(path,'ipol'):
	print 'you are not running the local version of ipol, this is not expected'
	raise


import ipol.new_wrappers

ipol.new_wrappers.run_all_examples()
