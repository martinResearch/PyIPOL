
from scipy.misc import imsave,imread
import ipol.tools as tools
import ipol.wrappers.TV_L1_Optical_Flow_Estimation as wrapper

def example():
   
   from matplotlib import pyplot as plt
   import numpy as np
   
   image1=imread(wrapper.source_directory+'/I0.png')
   image2=imread(wrapper.source_directory+'/I1.png')
   
   flow=wrapper.tvl1flow(image1,image2)
   plt.subplot(2,2,1)   
   plt.imshow(image1)
   plt.subplot(2,2,2)   
   plt.imshow(image2)
   plt.subplot(2,2,3)   
   plt.imshow(flow[:,:,0])   
   plt.subplot(2,2,4)   
   plt.imshow(flow[:,:,1])    
   plt.show()
   print 'done' 
   
   
if __name__ == '__main__':

   example()
