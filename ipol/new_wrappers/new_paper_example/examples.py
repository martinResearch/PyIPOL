from scipy.misc import imsave,imread
import ipol.new_wrappers.new_paper_example as wrapper
import matplotlib.pyplot as plt

def example():
   
   from matplotlib import pyplot as plt
   import numpy as np 

   # todo: read the example image from the papers source directory   
   image=imread(wrapper.source_directory+'/avs.jpg')# the scipy.misc.imread uses PIL which give an error for this bmp file (Unsupported BMP compression )
   
   # todo: call the wrapped function(s) with a valid set of arguments
   output=wrapper.ace(image,alpha=5,omega='1/r',method='interp',levels=5)

   # todo: display the results
   plt.subplot(1,2,1)   
   plt.imshow(image)
   plt.subplot(1,2,2)   
   plt.imshow(output)
   plt.show()
   print 'done' 


if __name__ == '__main__':

	example()


   
