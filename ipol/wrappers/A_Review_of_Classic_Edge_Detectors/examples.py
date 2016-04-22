from scipy.misc import imread
import matplotlib.pyplot as plt
import ipol.wrappers.A_Review_of_Classic_Edge_Detectors as wrapper
import numpy as np

def example():
	plt.ion()

	im_file =wrapper.source_directory+'lena.png'
	image=imread(im_file)
	plt.subplot(1,2,1)
	plt.imshow(image,cmap=plt.cm.Greys_r)

	edges=wrapper.edges_sobel(image.astype(np.float32),0.1,2)
	plt.subplot(1,2,2)
	plt.ioff()
	plt.imshow(edges)
	plt.show()

if __name__ == '__main__':

	example()


