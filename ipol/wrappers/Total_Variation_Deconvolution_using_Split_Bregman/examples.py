import os
from scipy.misc import imsave,imread
from skimage.io import imread as skimage_imread
import ipol.tools as tools
import ipol.wrappers.Total_Variation_Deconvolution_using_Split_Bregman as wrapper

def example():
   
   from matplotlib import pyplot as plt
   import cv2
   im_file =wrapper.source_directory+'/einstein.bmp'
   image=cv2.imread(im_file)
   blurry=wrapper.imblur(image, kernel='disk',radius=1,noise='gaussian',sigma=5)
   deconv=wrapper.tvdeconv(image, kernel='disk',radius=1,noise='gaussian',lamb=50)
   plt.subplot(1,3,1)
   plt.imshow(image)
   plt.subplot(1,3,2)
   plt.imshow(blurry, cmap='Greys_r')
   plt.subplot(1,3,3)
   plt.imshow(deconv, cmap='Greys_r')
   plt.show()
   print 'done' 
   
if __name__ == '__main__':
   example()

