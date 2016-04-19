# this script will download the original C++ codes from  IPOL and eventually patch some of the code

import urllib
import os
import zipfile
import tarfile

extraction_directory='./ipol/csources'

files=[]
# 3D 
files.append('http://www.ipol.im/pub/art/2014/81/BallPivoting.tgz') 	# An Analysis and Implementation of a Parallel Ball Pivoting Algorithm
files.append('http://www.ipol.im/pub/art/2015/102/scale-space-meshing_1.0.tgz')#An Implementation and Parallelization of the Scale Space Meshing Algorithm


# BLUR
files.append('http://www.ipol.im/pub/art/2013/87/gaussian_20131215.tgz')# A Survey of Gaussian Convolution Algorithms
files.append('http://www.ipol.im/pub/art/2012/g-tvdc/tvdeconv_20120607.tar.gz')#Total Variation Deconvolution using Split Bregman

# INPAINTING
files.append('http://www.ipol.im/pub/art/2015/136/inpaint_8.tgz')         # Variational Framework for Non-Local Inpainting
files.append('http://www.ipol.im/pub/art/2016/117/gaussconv_20160131.zip')# Computing an Exact Gaussian Scale-Space

# SEGMENTATION AND EDGES
files.append('http://www.ipol.im/pub/art/2015/35/classic_edge_detectors_1.0.zip')# A Review of Classic Edge Detectors
files.append('http://www.ipol.im/pub/art/2012/g-cv/chanvese_20120715.tar.gz')    # Chan-Vese Segmentation
files.append('http://www.ipol.im/pub/art/2012/gjmr-lsd/lsd_1.6.zip')             # LSD: a Line Segment Detector
files.append('http://www.ipol.im/pub/art/2012/abmh-rtmsa/MorphologicalSnakes_basic_20111228.zip') #A Real Time Morphological Snakes Algorithm
files.append('http://www.ipol.im/pub/art/2015/126/126.zip') #An Unsupervised Point Alignment Detection Algorithm





def download_all():
	for f in files:
		download_and_extract(f)
	

def download_and_extract(f):	
	print "downloading %s..."%f,

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
	print "done"




