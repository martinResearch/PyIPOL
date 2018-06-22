import tempfile   
import os
from imageio import imwrite,imread
import ipol.tools as tools
import subprocess
import ipol.wrappers.DCT_Image_Denoising_a_Simple_and_Effective_Image_Denoising_Algorithm as wrapper


def example():
   
   from matplotlib import pyplot as plt
   import numpy as np
   
   noise_free=imread(wrapper.source_directory+'/cinput.jpg')# the scipy.misc.imread uses PIL which give an error for this bmp file (Unsupported BMP compression )
   noisy=imread(wrapper.source_directory+'/cnoisy.jpg')
   output=wrapper.DCTdenoising(noisy,sigma=3,noise_free=noise_free)
   plt.subplot(2,2,1)   
   plt.imshow(noise_free)
   plt.subplot(2,2,2)   
   plt.imshow(noisy)
   plt.subplot(2,2,3)   
   plt.imshow(output)   
   plt.subplot(2,2,4)   
   plt.imshow(np.sum(np.abs(output.astype(np.float)-noise_free.astype(np.float)),axis=2)/5 ,cmap='Greys_r')    
   plt.show()
   print 'done' 


   
if __name__ == '__main__':
   example()
