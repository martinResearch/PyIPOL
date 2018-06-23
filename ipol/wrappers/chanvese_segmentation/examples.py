import tempfile   
import os
from imageio import imwrite,imread
import ipol.tools as tools
import subprocess
import ipol.wrappers.chanvese_segmentation as wrapper

def example():
   
   from matplotlib import pyplot as plt
   import cv2
   im_file =wrapper.source_directory+'/wrench.bmp'
   image=cv2.imread(im_file)# the scipy.misc.imread uses PIL which give an error for this bmp file (Unsupported BMP compression )
   output,animation=wrapper.chanvese(image)
   plt.ion()
   for frame in  animation:
      plt.imshow(frame)
      plt.draw()
      plt.show()
   plt.ioff()
   plt.imshow(output, cmap='Greys_r')
   plt.show()
   print ('done') 

if __name__ == '__main__':
   example()
