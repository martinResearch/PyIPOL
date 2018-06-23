import tempfile   
import os
from imageio import imwrite,imread
import ipol.tools as tools
import subprocess
import ipol.wrappers.Rudin_Osher_Fatemi_Total_Variation_Denoising_using_Split_Bregman as wrapper

def example():
   
   from matplotlib import pyplot as plt
   import numpy as np
   import cv2
   noise_free=np.mean(cv2.imread(wrapper.source_directory+'/einstein.bmp'),axis=2)# the scipy.misc.imread uses PIL which give an error for this bmp file (Unsupported BMP compression )
  
   noisy=wrapper.imnoise(noise_free,model='gaussian',sigma=15)
   output=wrapper.tvdenoise(noisy, model='gaussian',sigma=15)
   plt.subplot(2,2,1)   
   plt.imshow(noise_free,cmap='Greys_r')
   plt.subplot(2,2,2)   
   plt.imshow(noisy,cmap='Greys_r')
   plt.subplot(2,2,3)   
   plt.imshow(output,cmap='Greys_r')
   plt.subplot(2,2,4)   
   plt.imshow(np.abs(output.astype(np.float)-noise_free.astype(np.float))/5 ,cmap='Greys_r')    
   plt.show()
   print ('done') 
   
if __name__ == '__main__':
   import sys 
   if 'install' in sys.argv:
      _install()
   else:
      example()

