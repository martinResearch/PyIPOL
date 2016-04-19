import tempfile   
import os
from scipy.misc import imsave,imread
from skimage.io import imread as skimage_imread
import tools
import subprocess


string="""Rudin-Osher-Fatemi Total Variation Denoising using Split Bregman. Pascal Getreuer"""

path=os.path.dirname(__file__)

exec_folder=tools.extraction_directory+'/tvdenoise_20120516'
def _install():
   """this function downloads and compile the code for the chanvese implementation"""
   download_file='http://www.ipol.im/pub/art/2012/g-tvd/tvdenoise_20120516.tar.gz'
   tools.download_and_extract(download_file)  
   os.system( 'sudo apt-get install build-essential libjpeg8-dev libpng-dev libtiff-dev')
   this_file_path=os.path.dirname(__file__)
   subprocess.call('make -f makefile.gcc', shell=True,cwd=exec_folder)   
   
   

def tvdenoise(image,model,sigma):
   """
   Usage: tvdenoise <model>:<sigma> <noisy> <denoised>
   
   where <noisy> and <denoised> are BMP (JPEG, PNG, or TIFF files can also be 
   used if the program is compiled with libjpeg, libpng, and/or libtiff).
   The program reads image <noisy> and applies TV regularized denoising to 
   produce <denoised>.
   
   The <model> argument denotes the noise model.  The parameter <sigma>
   is the noise level, which is defined to be the square root of the
   expected mean squared error.
   
   The pixel intensities are denoted below by X[n] and Y[n], and they
   are scaled as values between 0 and 255.  Values of Y[n] outside of
   this range are saturated.
   
     gaussian:<sigma>  Additive white Gaussian noise
                       Y[n] ~ Normal(X[n], sigma^2)
                       p(Y[n]|X[n]) = exp( -|Y[n] - X[n]|^2/(2 sigma^2) )
   
     laplace:<sigma>   Laplace noise
                       Y[n] ~ Laplace(X[n], sigma/sqrt(2))
                       p(Y[n]|X[n]) = exp( -|Y[n] - X[n]| sqrt(2)/sigma )
   
     poisson:<sigma>   Poisson noise
                       Y[n] ~ Poisson(X[n]/a) a
                       where a = 255 sigma^2 / (mean value of X)
   """

   #saving input image to a temporary file
   output_file=tempfile.mkstemp('.PNG')[1]
   
   temp_image_file =tempfile.mkstemp('.PNG')[1]
   imsave(temp_image_file,image)
   assert(model in ['gaussian','laplace','poisson'])
  
   
   command=exec_folder+'/tvdenoise -n %s:%f %s %s'%(model,sigma,temp_image_file,output_file)
      
   # calling the executable
   os.system( command)   
   #reading the output from the temporary file
   output=imread(output_file)   
   os.remove(output_file)
   os.remove(temp_image_file)
   return output

def imnoise(image,model,sigma):
   """
   Syntax: imnoise <model>:<sigma> <input> <output>

The program reads the image <input> and simulates noise to create <output>.
The <model>:<sigma> argument has the same meaning as in tvdenoise.

   """

   #saving input image to a temporary file
   output_file=tempfile.mkstemp('.PNG')[1]
   
   temp_image_file =tempfile.mkstemp('.PNG')[1]
   imsave(temp_image_file,image)
   assert(model in ['gaussian','laplace','poisson'])
  
   
   command=exec_folder+'/imnoise %s:%f %s %s'%(model,sigma,temp_image_file,output_file)
      
   # calling the executable
   os.system( command)   
   #reading the output from the temporary file
   output=imread(output_file)   
   os.remove(output_file)
   os.remove(temp_image_file)   
   return output

def example():
   
   from matplotlib import pyplot as plt
   import numpy as np
   import cv2
   noise_free=np.mean(cv2.imread(exec_folder+'/einstein.bmp'),axis=2)# the scipy.misc.imread uses PIL which give an error for this bmp file (Unsupported BMP compression )
  
   noisy=imnoise(noise_free,model='gaussian',sigma=15)
   output=tvdenoise(noisy, model='gaussian',sigma=15)
   plt.subplot(2,2,1)   
   plt.imshow(noise_free,cmap='Greys_r')
   plt.subplot(2,2,2)   
   plt.imshow(noisy,cmap='Greys_r')
   plt.subplot(2,2,3)   
   plt.imshow(output,cmap='Greys_r')
   plt.subplot(2,2,4)   
   plt.imshow(np.abs(output.astype(np.float)-noise_free.astype(np.float))/5 ,cmap='Greys_r')    
   plt.show()
   print 'done' 
   
if __name__ == '__main__':
   import sys 
   if 'install' in sys.argv:
      _install()
   else:
      example()




