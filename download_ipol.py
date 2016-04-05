# this script will download the original C++ codes from  IPOL and eventually patch some of the code

import urllib
import os
import zipfile
import tarfile

files=[]
# 3D 
files.append('http://www.ipol.im/pub/art/2014/81/BallPivoting.tgz')
files.append('http://www.ipol.im/pub/pre/102/scale-space-meshing_1.0.tgz')

# BLUR
files.append('http://www.ipol.im/pub/art/2013/87/gaussian_20131215.tgz')
files.append('http://www.ipol.im/pub/art/2012/g-tvdc/tvdeconv_20120607.tar.gz')
files.append('http://www.ipol.im/pub/pre/136/inpaint_5.tgz')
files.append('http://www.ipol.im/pub/pre/116/filtering_1.00.tar.gz')
files.append('http://www.ipol.im/pub/pre/117/gaussconv_20140515.zip')

# SEGMENTATION AND EDGES
files.append('http://www.ipol.im/pub/art/2015/35/classic_edge_detectors_1.0.zip')
files.append('http://www.ipol.im/pub/art/2012/g-cv/chanvese_20120715.tar.gz')
files.append('http://www.ipol.im/pub/art/2012/gjmr-lsd/lsd_1.6.zip')
files.append('http://www.ipol.im/pub/art/2012/abmh-rtmsa/MorphologicalSnakes_basic_20111228.zip')
files.append('http://www.ipol.im/pub/pre/126/126.zip')


extraction_directory='./csources'
for f in files:
	print "downloading %s"%f
	
	local_filename, headers = urllib.urlretrieve(f)
	if f[-3:]=='zip':
		with zipfile.ZipFile(local_filename) as zf:
			zf.extractall(extraction_directory)
	elif f[-2:]=='gz':
		with tarfile.open(local_filename, "r") as tar:
			tar.extractall(extraction_directory)
	else:
		print 'unrecognized archive type'
		raise


