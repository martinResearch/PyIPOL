import tempfile   
import os
from scipy.misc import imsave,imread
from skimage.io import imread as skimage_imread
import tools
import subprocess


string="""Non-Local Means Denoising
Antoni Buades, Bartomeu Coll, Jean-Michel Morel"""

path=os.path.dirname(__file__)

exec_folder=tools.extraction_directory+'/nlmeansC'
def _install():
   """this function downloads and compile the code for the chanvese implementation"""
   download_file='http://www.ipol.im/pub/art/2011/bcm_nlm/nlmeansC.tar.gz'
   tools.download_and_extract(download_file)  
   import urllib
   # getting example images
   urllib.urlretrieve('http://www.ipol.im/pub/art/2011/bcm_nlm/cinput.jpg',os.path.join(exec_folder,'cinput.jpg'))
   urllib.urlretrieve('http://www.ipol.im/pub/art/2011/bcm_nlm/cnoisy.jpg',os.path.join(exec_folder,'cnoisy.jpg'))
   os.system( 'sudo apt-get install build-essential libjpeg8-dev libpng-dev libtiff-dev')
   this_file_path=os.path.dirname(__file__)
   subprocess.call('make', shell=True,cwd=exec_folder)   
   
   

def nlmeans(image,sigma,noise_free=None):
   """
   `nlmeans_ipol ` takes 4 parameter: `nlmeans_ipol in.png sigma noisy.png denoised.png`
   * `sigma`     : the noise standard deviation
   * `in.png`   : initial noise free image
   * `noisy.png`  : noisy image used by the denoising algorithm
   * `denoised.png` : denoised image
   """

   #saving input image to a temporary file
   output_file=tempfile.mkstemp()[1]+'.PNG'
   
   temp_image_file =tempfile.mkstemp()[1]+'.PNG'
   imsave(temp_image_file,image)
   
   if not noise_free is None:
      temp_noise_free_image_file =tempfile.mkstemp()[1]+'.PNG'
      imsave(temp_noise_free_image_file,noise_free)
   else:
      temp_noise_free_image_file=temp_image_file
   
   command=exec_folder+'/nlmeans_ipol %s %f %s %s'%(temp_noise_free_image_file,sigma,temp_image_file,output_file)
      
   # calling the executable
   os.system( command)   
   #reading the output from the temporary file
   output=imread(output_file)   
   return output

def example():
   
   from matplotlib import pyplot as plt
   import numpy as np
   
   noise_free=imread(exec_folder+'/cinput.jpg')# the scipy.misc.imread uses PIL which give an error for this bmp file (Unsupported BMP compression )
   noisy=imread(exec_folder+'/cnoisy.jpg')
   output=nlmeans(noisy,sigma=3,noise_free=noise_free)
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




