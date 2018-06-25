from imageio import imwrite,imread
import ipol.wrappers.Robust_Optical_Flow_Estimation as wrapper
import matplotlib.pyplot as plt



def example():
   
   from matplotlib import pyplot as plt
   import numpy as np
   
   image1=imread(wrapper.source_directory+'/spatial/I1.png')

 
   
   flow=wrapper.spatial(image1,image2)
   plt.subplot(2,2,1)   
   plt.imshow(image1,cmap='Greys_r')
   plt.subplot(2,2,2)   
   plt.imshow(image2,cmap='Greys_r')
   plt.subplot(2,2,3)   
   plt.imshow(flow[:,:,0],cmap='Greys_r') 
   plt.subplot(2,2,4)
   plt.imshow(flow[:,:,1],cmap='Greys_r')  
   
   
   images=[imread(wrapper.source_directory+'/temporal/images/frame%02d.png'%i) for i in range(6)]
   flows=wrapper.temporal(images)
   plt.figure()
   nbplot=len(flows)
   for i in range(nbplot):
        
      flow=flows[i]
      plt.subplot(2,nbplot,i+1) 
      plt.imshow(flow[:,:,0],cmap='Greys_r') 
      plt.subplot(2,nbplot,i+1+nbplot) 
      plt.imshow(flow[:,:,1],cmap='Greys_r')
   
   plt.show()
   
   
   print ('done') 
   
   
if __name__ == '__main__':

   example()


   
