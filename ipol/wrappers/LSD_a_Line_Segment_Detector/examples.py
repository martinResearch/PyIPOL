from scipy.misc import imread,imresize
import matplotlib.pyplot as plt
import numpy as np
import ipol.wrappers.LSD_a_Line_Segment_Detector as lsd	
from ipol.thirdparties import netpbmfile
import ipol.tools
import os

def example():
	plt.ion()

	im_file =os.path.join(lsd.source_directory,'chairs.pgm')

	#image =imread(im_file)# does not work with the provided pgm file :(

	image=netpbmfile.imread(im_file)
	plt.imshow(image,cmap=plt.cm.Greys_r)

	segments=lsd.lsd(image)
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
	example()


