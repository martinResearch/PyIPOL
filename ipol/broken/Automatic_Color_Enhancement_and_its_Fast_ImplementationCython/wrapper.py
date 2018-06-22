import tempfile   
import os
from imageio import imwrite,imread
from skimage.io import imread as skimage_imread
import ipol.tools as tools
import subprocess
import _wrapper

string="""Automatic Color Enhancement (ACE) and its Fast Implementation
Pascal Getreuer"""

path=os.path.dirname(__file__)

exec_folder=tools.extraction_directory+'/ace_20121029'
source_directory=exec_folder

def ace(image,alpha,omega,sigma=None,method='interp',levels=None,degree=None,jpeg_quality=100):
   """
   Usage: ace [options] input output
   
   where "input" and "output" are BMP files (JPEG, PNG, or TIFF files can also 
   be used if the program is compiled with libjpeg, libpng, and/or libtiff).  
   
   Options:
     -a <number>  alpha, stronger implies stronger enhancement
     -w <omega>   omega, spatial weighting function, choices are
                  1/r      default ACE, omega(x,y) = 1/sqrt(x^2+y^2)
                  1        constant, omega(x,y) = 1
                  G:#      Gaussian, where # specifies sigma,
                           omega(x,y) = exp(-(x^2+y^2)/(2 sigma^2))
     -m <method>  method to use for fast computation, choices are
                  interp:# interpolate s_a(L - I(x)) with # levels
                  poly:#   polynomial s_a with degree #
   
     -q <number>  quality for saving JPEG images (0 to 100)
   """

   #saving input image to a temporary file
   output_file=tempfile.mkstemp('.PNG')[1]
   
   temp_image_file =tempfile.mkstemp('.PNG')[1]
   imwrite(temp_image_file,image)


   if method=='interp':
      method_str='interp:%d'%levels
      assert(degree is None)
   elif ethod=='poly':
      method_str='poly:%d'%degree
      assert(levels is None)
   if omega=='G':
      omega_str='G %f'%sigma
   else:
      omega_str=omega
      assert(sigma is None)
   
   options='-a %f -w %s -m %s %s %s'%(alpha,omega_str,method_str,temp_image_file,output_file)
   if False: #using the executable
      command=exec_folder+'/ace %s'%options
      # calling the executable
      os.system( command)
   else:
      print options.split(' ')
      _wrapper.main(options.split(' '))
   #reading the output from the temporary file
   output=imread(output_file)  
   os.remove(output_file)

   os.remove(temp_image_file)
   return output







