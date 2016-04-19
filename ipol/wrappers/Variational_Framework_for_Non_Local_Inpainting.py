import tempfile   
import os
from scipy.misc import imsave,imread
from skimage.io import imread as skimage_imread
import tools
import subprocess
import glob
from subprocess import Popen, PIPE, STDOUT



string="""Variational Framework for Non-Local Inpainting
Vadim Fedorov, Gabriele Facciolo, Pablo Arias
http://www.ipol.im/pub/art/2015/136/"""

exec_folder=tools.extraction_directory+'/inpaint_9'

def _install():
   """this function downloads and compile the code for the inpainting implementation"""
   download_file='http://www.ipol.im/pub/art/2015/136/inpaint_8.tgz'
   tools.download_and_extract(download_file)  
   os.system( 'sudo apt-get install build-essential libjpeg8-dev libpng-dev libtiff-dev')
   this_file_path=os.path.dirname(__file__)
   subprocess.call(' mkdir build; cd build; cmake ..; make', shell=True,cwd=exec_folder)   
  
   

def inpaint(image,mask,method='nlmeans',patch=9,iters=300,scales=7,coarse=0.3,conft=5,confa=0.1,lamb=0.05,init='poisson',psigma=10000):
   """
   options
       -method    method name (nlmeans)
       -patch     patch side (9)
       -iters     inpainting iterations (300)
       -scales    scales amount (7)
       -coarse    coarsest rate (0.3)
       -conft     confidence decay time (5)
       -confa     confidence asymptotic value (0.1)
       -lambda    lambda (0.05)
       -init      initialization type [poisson/black/avg/none] (poisson)
       -psigma    Gaussian patch weights (10000)
       -showpyr   PREFIX write intermediate pyramid results
       -shownnf   FILENAME write illustration of the final NNF
   """

   #saving input image to a temporary file
   output_file=tempfile.mkstemp('.PNG' )[1]  
   image_file =tempfile.mkstemp('.PNG')[1]
   imsave(image_file,image)
   mask_file =tempfile.mkstemp('.PNG')[1]
   imsave(mask_file,mask)

   command=exec_folder+'/build/Inpainting %s %s %s'%(image_file,mask_file,output_file)
   command+=' -method %s'%method
   command+=' -patch %d'%patch
   command+=' -iters %d'%iters
   command+=' -scales %d'%scales
   command+=' -coarse %f'%coarse
   command+=' -conft %f'%conft
   command+=' -confa %f'%confa
   command+=' -lambda %f'%lamb
   command+=' -init%s'%init
   command+=' -psigma %f'%psigma
     
   # calling the executable
   #subprocess.call( command ,shell=True)
   p = Popen(command, stdout = PIPE, stderr = PIPE,bufsize=1,shell=True)
   for line in iter(p.stdout.readline, ''):
      print line
   p.stdout.close()   
   p.wait()
   #reading the output from the temporary file
   
   l=glob.glob(output_file+'_*')# trick because the output file name is not excactly the one expected , things are added at the end
   assert(len(l)==1)
   output=imread(l[0])
   os.remove(l[0])
   os.remove(output_file)
   os.remove(image_file)
   os.remove(mask_file)
   return output

def example():
   
   from matplotlib import pyplot as plt
   import cv2
   im_file =exec_folder+'/data/kom07.png'
   mask_file =exec_folder+'/data/kom07_msk.png'
   image=imread(im_file)# the scipy.misc.imread uses PIL which give an error for this bmp file (Unsupported BMP compression )
   mask=cv2.imread(mask_file)# for some strange reason scipy.misc.imread is not able to read that image properly
   output=inpaint(image,mask)
   plt.subplot(1,3,1)
   plt.imshow(image)
   plt.subplot(1,3,2)
   plt.imshow(mask)
   plt.subplot(1,3,3)
   plt.imshow(output)
   plt.show()
   print 'done' 
   
if __name__ == '__main__':
   #_install()
   example()




