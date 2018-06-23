from imageio import imwrite,imread
import ipol.wrappers.ASIFT_An_Algorithm_for_Fully_Affine_Invariant_Comparison as wrapper
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
def example():
   
   from matplotlib import pyplot as plt
   import numpy as np 

   # todo: read the example image from the papers source directory   
   image1=imread(wrapper.source_directory+'/adam1.png') 
   image2=imread(wrapper.source_directory+'/adam2.png')
   
   # todo: call the wrapped function(s) with a valid set of arguments
   matches,keys1,keys2=wrapper.asift(image1,image2)

   # todo: display the results
   fig = plt.figure(figsize=(10,5))
   ax1 = fig.add_subplot(121)
   plt.imshow(image1,cmap='Greys_r') 
   ax2 = fig.add_subplot(122)
   plt.imshow(image2,cmap='Greys_r')   


   for x1,y1,x2,y2 in matches[::1,:]:
      con = ConnectionPatch(xyA=(x2, y2), xyB=(x1,y1),  coordsA="data", coordsB="data"  ,
                            axesA=ax2, axesB=ax1,
                            shrinkB=5,color='r')
      ax2.add_artist(con)
   plt.draw()
   plt.show()

   print ('done' )


if __name__ == '__main__':

	example()


   
