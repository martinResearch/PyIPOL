import tempfile   
import os
from imageio import imwrite,imread
import ipol.tools as tools
import subprocess


string="""Implementation of the "Non-Local Bayes" (NL-Bayes) Image Denoising Algorithm
Marc Lebrun, Antoni Buades, Jean-Michel Morel"""

path=os.path.dirname(__file__)

exec_folder=tools.extraction_directory+'/nl-bayes_20130617'
source_directory=exec_folder

def NL_Bayes(image,sigma,noise_free=None,UseArea1=1,UseArea2=0,compute_bias=0):
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
   
   ImBasic_file     = tempfile.mkstemp('.PNG')[1]
   ImDiff_file      = tempfile.mkstemp('.PNG')[1]
   ImBias_file      = tempfile.mkstemp('.PNG')[1]
   ImBiasBasic_file  = tempfile.mkstemp('.PNG')[1]
   ImDiffBias_file  = tempfile.mkstemp('.PNG')[1]
   temp_folder=tempfile.mkdtemp()
   
   
   if not noise_free is None:
      temp_noise_free_image_file =tempfile.mkstemp('.PNG')[1]
      imwrite(temp_noise_free_image_file,noise_free)
   else:
      temp_noise_free_image_file=temp_image_file
   #./demo_DCTdenoising cinput.png 10 ImNoisy.png ImDenoised.png ImDiff.png
   command='cd %s'%temp_folder+';'+exec_folder+'/NL_Bayes %s %f %s %s %s %s %s %s %s %d %d %d'%(temp_noise_free_image_file,sigma,temp_image_file,output_file,ImBasic_file,ImDiff_file,ImBias_file,ImBiasBasic_file,ImDiffBias_file ,UseArea1,UseArea2,compute_bias)
      
   # calling the executable
   os.system( command)   
   #reading the output from the temporary file
   output=imread(output_file)  
   os.remove(output_file)
   if not noise_free is None:
      os.remove(temp_noise_free_image_file)
   os.remove(ImBasic_file)
   os.remove(ImDiff_file )
   os.remove(ImBias_file      )
   os.remove(ImBiasBasic_file  )
   os.remove(ImDiffBias_file )   
   os.remove(temp_image_file)
   os.remove(os.path.join(temp_folder,'measures.txt'))
   os.rmdir(temp_folder)
   return output


   



