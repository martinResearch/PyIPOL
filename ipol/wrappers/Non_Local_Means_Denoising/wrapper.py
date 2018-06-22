import tempfile   
import os
from imageio import imwrite,imread
import ipol.tools as tools
import subprocess


string="""Non-Local Means Denoising
Antoni Buades, Bartomeu Coll, Jean-Michel Morel"""

path=os.path.dirname(__file__)

exec_folder=tools.extraction_directory+'/nlmeansC'
source_directory=exec_folder

def nlmeans(image,sigma,noise_free=None):
   """
   `nlmeans_ipol ` takes 4 parameter: `nlmeans_ipol in.png sigma noisy.png denoised.png`
   * `sigma`     : the noise standard deviation
   * `in.png`   : initial noise free image
   * `noisy.png`  : noisy image used by the denoising algorithm
   * `denoised.png` : denoised image
   """

   #saving input image to a temporary file
   output_file=tempfile.mkstemp('.PNG')[1]
   
   temp_image_file =tempfile.mkstemp('.PNG')[1]
   imwrite(temp_image_file,image)
   
   if not noise_free is None:
      temp_noise_free_image_file =tempfile.mkstemp('.PNG')[1]
      imwrite(temp_noise_free_image_file,noise_free)
   else:
      temp_noise_free_image_file=temp_image_file
   
   command=exec_folder+'/nlmeans_ipol %s %f %s %s'%(temp_noise_free_image_file,sigma,temp_image_file,output_file)
      
   # calling the executable
   os.system( command)   
   #reading the output from the temporary file
   output=imread(output_file)  
   os.remove(output_file)
   if not noise_free is None:
      os.remove(temp_noise_free_image_file)
   os.remove(temp_image_file)
   return output


   
if __name__ == '__main__':
   import sys 
   if 'install' in sys.argv:
      _install()





