from scipy.misc import imsave,imread
#import ipol.wrappers.Automatic_Color_Enhancement_and_its_Fast_Implementation as wrapper
import wrapper
import matplotlib.pyplot as plt

def example():
   
   from matplotlib import pyplot as plt
   import numpy as np   
   image=imread(wrapper.source_directory+'/avs.jpg')# the scipy.misc.imread uses PIL which give an error for this bmp file (Unsupported BMP compression )
   
   output=wrapper.ace(image,alpha=5,omega='1/r',method='interp',levels=5)
   plt.subplot(1,2,1)   
   plt.imshow(image)
   plt.subplot(1,2,2)   
   plt.imshow(output)
   plt.show()
   print 'done' 


if __name__ == '__main__':

	example()


   
