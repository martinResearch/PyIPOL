from imageio import imwrite,imread
import ipol.wrappers.Stereo_Disparity_through_Cost_Aggregation_with_Guided_Filter as wrapper
import matplotlib.pyplot as plt
import os

def example():
   
   from matplotlib import pyplot as plt
   import numpy as np 

   # todo: read the example image from the papers source directory   
   image1=imread(os.path.join(wrapper.source_directory,'data','tsukuba0.png')) 
   image2=imread(os.path.join(wrapper.source_directory,'data','tsukuba1.png')) 
  

   output=wrapper.stereoGuidedFilter(image1,image2,dmin=-15,dmax=0)
   print ('found disparities :')
   v,c=np.unique(output['disparity'],return_counts=True)
   plt.plot(v,c)
   plt.title('nb pixel per disparity')
   # todo: display the results
   plt.figure()
   plt.subplot(2,2,1)   
   plt.imshow(output['disparity'].astype(np.float),cmap='Greys_r')
   plt.subplot(2,2,2)   
   plt.imshow(output['occlusion'].astype(np.float),cmap='Greys_r')
   plt.subplot(2,2,3)   
   plt.imshow(output['occlusion_filled'].astype(np.float),cmap='Greys_r')
   plt.subplot(2,2,4)   
   plt.imshow(output['occlusion_filled_smoothed'].astype(np.float),cmap='Greys_r')
   plt.show()
   print ('done' )

if __name__ == '__main__':

   example()


   
