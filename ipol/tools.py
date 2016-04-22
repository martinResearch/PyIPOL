# this script will download the original C++ codes from  IPOL and eventually patch some of the code

import urllib
import os
import zipfile
import tarfile
from PIL import Image
import numpy as np

path=os.path.dirname(__file__)
extraction_directory=os.path.join(path,'csources')


def download_and_extract(f,subfolder=''):	
	print "downloading %s..."%f,

	local_filename, headers = urllib.urlretrieve(f)
	if f[-3:]=='zip':
		with zipfile.ZipFile(local_filename) as zf:
			zf.extractall(extraction_directory+subfolder)
	elif f[-2:]=='gz':
		with tarfile.open(local_filename, "r") as tar:
			tar.extractall(extraction_directory+subfolder)
	else:
		print 'unrecognized archive type'
		raise
	print "done"
	
	
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





