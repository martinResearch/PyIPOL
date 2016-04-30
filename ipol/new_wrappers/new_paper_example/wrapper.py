import tempfile   
import os
from scipy.misc import imsave,imread
from skimage.io import imread as skimage_imread
import ipol.tools as tools
import subprocess
from install import source_directory


string="""Automatic Color Enhancement (ACE) and its Fast Implementation
Pascal Getreuer""" # todo: put the name of the paper you are adding to PyIPOL

path=os.path.dirname(__file__)


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
   """# todo : copy the documentation from the C++ file
  
   # todo: create temporary files names for unput and outputs that are files for the executable (images for example)
   # and save input images 

   output_file=tempfile.mkstemp('.PNG')[1]   
   temp_image_file =tempfile.mkstemp('.PNG')[1] 
   imsave(temp_image_file,image)

   # todo : generate the command to execute the executable with the right options
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
   command=source_directory+'/ace -a %f -w %s -m %s %s %s'%(alpha,omega_str,method_str,temp_image_file,output_file)
      
   # calling the executable
   os.system( command)   

   #todo: read the output from the temporary file
   output=imread(output_file)  

   # todo : delete the temporary files
   os.remove(output_file)
   os.remove(temp_image_file)

   return output




