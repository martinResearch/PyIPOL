from scipy.misc import imread,imresize
import matplotlib.pyplot as plt
import numpy as np
import ipol
from ipol.thirdparties import netpbmfile
import tools

def _install():

   	download_file='http://www.ipol.im/pub/art/2012/gjmr-lsd/lsd_1.6.zip'
   	tools.download_and_extract(download_file)  
	pass

def example():
	plt.ion()

	im_file =ipol.path+'/csources/lsd_1.6/chairs.pgm'

	#image =imread(im_file)# does not work with the provided pgm file :(

	image=netpbmfile.imread(im_file)
	plt.imshow(image,cmap=plt.cm.Greys_r)

	segments=ipol.lsd(image)
	print 'found '+str( segments.shape[0]),' segments'

	plt.figure()
	#plt.ion()
	plt.imshow(image,cmap=plt.cm.Greys_r)
	for seg in segments:
		plt.plot(seg[[0,2]],seg[[1,3]])
	plt.axis('tight')
	plt.ioff()

	plt.show()

if __name__ == '__main__':
   import sys 
   if 'install' in sys.argv:
      _install()
   else:
      example()

