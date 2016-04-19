from scipy.misc import imread,imresize
import matplotlib.pyplot as plt
import numpy as np
import ipol
from ipol.thirdparties import netpbmfile
import tools

def _install():
	"""this function downloads and compile the code for the chanvese implementation"""
	download_file='http://www.ipol.im/pub/art/2015/35/classic_edge_detectors_1.0.zip'
	tools.download_and_extract(download_file)  

def example():
	plt.ion()

	im_file =ipol.path+'/csources/lsd_1.6/chairs.pgm'

	#image =imread(im_file)# does not work with the provided pgm file :(

	image=netpbmfile.imread(im_file)
	plt.imshow(image,cmap=plt.cm.Greys_r)

	edges=ipol.edges_sobel(image.astype(np.float32),0.1,2)
	plt.imshow(edges)

if __name__ == '__main__':
   import sys 
   if 'install' in sys.argv:
      _install()
   else:
      example()


