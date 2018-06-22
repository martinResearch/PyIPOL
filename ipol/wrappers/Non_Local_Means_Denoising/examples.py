import tempfile   
import os
from imageio import imwrite,imread
import ipol.tools as tools
import subprocess

import ipol.wrappers.Non_Local_Means_Denoising as wrapper


def example():
   
   from matplotlib import pyplot as plt
   import numpy as np
   
   noise_free=imread(wrapper.source_directory+'/cinput.jpg')# the scipy.misc.imread uses PIL which give an error for this bmp file (Unsupported BMP compression )
   noisy=imread(wrapper.source_directory+'/cnoisy.jpg')
   output=wrapper.nlmeans(noisy,sigma=3,noise_free=noise_free)
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
   import sys 
   if 'install' in sys.argv:
      _install()
   else:
      example()

