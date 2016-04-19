import tempfile   
import os
from scipy.misc import imsave,imread
from skimage.io import imread as skimage_imread
import tools
import subprocess
import glob
from subprocess import Popen, PIPE, STDOUT

string='''Total Variation Deconvolution using Split Bregman
Pascal Getreuer
http://www.ipol.im/pub/art/2012/g-tvdc/'''


exec_folder=tools.extraction_directory+'/tvdeconv_20120607'
def _install():
   """this function downloads and compile the code for the tvdeconv implementation"""
   download_file='http://www.ipol.im/pub/art/2012/g-tvdc/tvdeconv_20120607.tar.gz'
   tools.download_and_extract(download_file)  
   this_file_path=os.path.dirname(__file__)
   subprocess.call('make -f makefile.gcc', shell=True,cwd=exec_folder)   
  
   

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
   imsave(image_file,image)
 

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
   imsave(image_file,image)
 

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

def example():
   
   from matplotlib import pyplot as plt
   import cv2
   im_file =exec_folder+'/einstein.bmp'
   image=cv2.imread(im_file)
   blurry=imblur(image, kernel='disk',radius=1,noise='gaussian',sigma=5)
   deconv=tvdeconv(image, kernel='disk',radius=1,noise='gaussian',lamb=50)
   plt.subplot(1,3,1)
   plt.imshow(image)
   plt.subplot(1,3,2)
   plt.imshow(blurry, cmap='Greys_r')
   plt.subplot(1,3,3)
   plt.imshow(deconv, cmap='Greys_r')
   plt.show()
   print 'done' 
   
if __name__ == '__main__':
   #_install()
   example()




