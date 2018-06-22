import tempfile   
import os
from imageio import imwrite,imread
import ipol.tools as tools
import subprocess
import glob
from subprocess import Popen, PIPE, STDOUT

string='''Total Variation Deconvolution using Split Bregman
Pascal Getreuer
http://www.ipol.im/pub/art/2012/g-tvdc/'''


exec_folder=tools.extraction_directory+'/tvdeconv_20120607'
source_directory=exec_folder

def tvdeconv(image,kernel,radius=None,sigma_kernel=None,lamb=50,noise='gaussian',jpegquality=100):
   """
   Parameters
     K:<kernel>             blur kernel for deconvolution
         K:disk:<radius>         filled disk kernel
         K:gaussian:<sigma>      Gaussian kernel
         K:<file>                read kernel from text or image file
     lambda:<value>         fidelity weight
     noise:<model>          noisy model
         noise:gaussian          additive Gaussian noise (default)
         noise:laplace           Laplace noise
         noise:poisson           Poisson noise
     f:<file>               input file (alternative syntax)
     u:<file>               output file (alternative syntax)
     jpegquality:<number>   quality for saving JPEG images (0 to 100)
   """
   
   
   assert(noise in ['gaussian','laplace','poisson'])
   
   #saving input image to a temporary file
   output_file=tempfile.mkstemp('.PNG')[1]    
   image_file =tempfile.mkstemp('.PNG')[1]
   imwrite(image_file,image)
 

   command=exec_folder+'/tvdeconv %s %s'%(image_file,output_file)
   if kernel=='disk':
      command+=' K:disk:%s'%(radius)
      assert(sigma_kernel is None)
      
   elif kernel=='gaussian':
      command+=' K:gaussian:%s'%(sigma_kernel)
      assert(radius is None)
      
   elif isinstance(kernel,np.array) :
      pass
   
   
   command+=' lambda:%f'%lamb
   
   command+=' noise:%s'%noise
     
   # calling the executable
   #subprocess.call( command ,shell=True)
   p = Popen(command, stdout = PIPE, stderr = PIPE,bufsize=1,shell=True)
   for line in iter(p.stdout.readline, ''):
      print line
   p.stdout.close()   
   p.wait()
   #reading the output from the temporary file
   
  
   output=imread(output_file)
   os.remove(output_file)
   os.remove(image_file)   
   return output

def imblur(image,kernel,radius=None,sigma_kernel=None,noise='gaussian',sigma=2,jpegquality=100):
   """
   The imblur program blurs and adds noise to an image.
   
   Parameters
     K:<kernel>             blur kernel for deconvolution
         K:disk:<radius>         filled disk kernel
         K:gaussian:<sigma>      Gaussian kernel
         K:<file>                read kernel from text or image file
     noise:<model>:<sigma>  simulate noise with standard deviation sigma
         noise:gaussian:<sigma>  additive white Gaussian noise
         noise:laplace:<sigma>   Laplace noise
         noise:poisson:<sigma>   Poisson noise
     f:<file>               input file (alternative syntax)
     u:<file>               output file (alternative syntax)
     jpegquality:<number>   quality for saving JPEG images (0 to 100)
   """
   
   
   assert(noise in ['gaussian','laplace','poisson'])
   
   #saving input image to a temporary file
   output_file=tempfile.mkstemp('.PNG' )[1] 
   image_file =tempfile.mkstemp('.PNG')[1]
   imwrite(image_file,image)
 

   command=exec_folder+'/imblur %s %s'%(image_file,output_file)
   if kernel=='disk':
      command+=' K:disk:%s'%(radius)
      assert(sigma_kernel is None)
      
   elif kernel=='gaussian':
      command+=' K:gaussian:%s'%(sigma_kernel)
      assert(radius is None)
      
   elif isinstance(kernel,np.array) :
      pass
   
   
   
   command+=' noise:%s:%f'%(noise,sigma)
     
   # calling the executable
   #subprocess.call( command ,shell=True)
   p = Popen(command, stdout = PIPE, stderr = PIPE,bufsize=1,shell=True)
   for line in iter(p.stdout.readline, ''):
      print line
   p.stdout.close()   
   p.wait()
   #reading the output from the temporary file
   
  
   output=imread(output_file)
   os.remove(output_file)
   os.remove(image_file)
   return output





