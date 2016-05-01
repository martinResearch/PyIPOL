from scipy.misc import imsave,imread
import ipol.wrappers.An_Analysis_of_the_SURF_Method as wrapper
import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.patches import ConnectionPatch
def example():
   
   
 
   # todo: read the example image from the papers source directory   
   image1=imread(wrapper.source_directory+'/examples/gobelet.png') 
   image2=imread(wrapper.source_directory+'/examples/gobelet2.png')
   
   # todo: call the wrapped function(s) with a valid set of arguments
   #keys1=wrapper.
   keys1=wrapper.extract_surf(image1)
   keys2=wrapper.extract_surf(image2)
   matches=wrapper.match_surf(keys1,keys2)

   # todo: display the results
   fig = plt.figure(figsize=(10,5))
   ax1 = fig.add_subplot(121)
   plt.imshow(image1) 
   ax2 = fig.add_subplot(122)
   plt.imshow(image2)     
  
 
   for x1,y1,x2,y2 in matches:
      con = ConnectionPatch(xyA=(x2, y2), xyB=(x1,y1),  coordsA="data", coordsB="data"  ,
                         axesA=ax2, axesB=ax1,
                         shrinkB=5,color='r')
      ax2.add_artist(con)
   plt.draw()
   plt.show()
 
   
   
   print 'done' 


if __name__ == '__main__':

	example()


   
