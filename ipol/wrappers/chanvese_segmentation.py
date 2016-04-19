import tempfile   
import os
from scipy.misc import imsave,imread
from skimage.io import imread as skimage_imread
import tools
import subprocess


string="""Chan-Vese Segmentation 
Pascal Getreuer
http://www.ipol.im/pub/art/2012/g-cv"""

path=os.path.dirname(__file__)

exec_folder=tools.extraction_directory+'/chanvese_20120715'
def _install():
   """this function downloads and compile the code for the chanvese implementation"""
   download_file='http://www.ipol.im/pub/art/2012/g-cv/chanvese_20120715.tar.gz'
   tools.download_and_extract(download_file)  
   os.system( 'sudo apt-get install build-essential libjpeg8-dev libpng-dev libtiff-dev')
   this_file_path=os.path.dirname(__file__)
   subprocess.call('make -f makefile.gcc', shell=True,cwd=exec_folder)   
   
   

def chanvese(image,mu=0.25,nu=0.0,lambda1=1.0,lambda2=1.0,phi0=None,tol=1.e-4,maxiter=500,dt=0.5,iterperframe=10,getAnimation=True):
   """
   mu:<number>           length penalty (default 0.25)
   nu:<number>           area penalty (default 0.0)
   lambda1:<number>      fit weight inside the cuve (default 1.0)
   lambda2:<number>      fit weight outside the curve (default 1.0)
   phi0:<file>           read initial level set from an array
   tol:<number>          convergence tolerance (default 1e-4)
   maxiter:<number>      maximum number of iterations (default 500)
   dt:<number>           time step (default 0.5)
   iterperframe:<number> iterations per frame (default 10)
   """

   #saving input image to a temporary file
   output_file=tempfile.mkstemp()[1]+'.PNG' 
   animation_file=tempfile.mkstemp()[1]+'.gif'
   temp_image_file =tempfile.mkstemp()[1]+'.PNG'
   imsave(temp_image_file,image)

   if not phi0 is None:
      temp_phi0_file
      imsave(temp_phi0_file,phi0)
      command=exec_folder+'/chanvese mu:%f nu:%f lambda1:%f lambda2:%f phi0:%s tol:%f maxiter:%d dt:%f iterperframe:%d %s %s %s'%(mu,nu,lambda1,lambda2,temp_phi0_file,tol,maxiter,dt,iterperframe,temp_image_file,animation_file,output_file)
   else:
      command=exec_folder+'/chanvese mu:%f nu:%f lambda1:%f lambda2:%f tol:%f maxiter:%d dt:%f iterperframe:%d %s %s %s'%(mu,nu,lambda1,lambda2,tol,maxiter,dt,iterperframe,temp_image_file,animation_file,output_file)
      
   # calling the executable
   os.system( command)
   
   #reading the output from the temporary file
   output=imread(output_file)
   
   if getAnimation:
      animation=tools.read_animated_gif(animation_file)
      return output,animation
   else:
      return output

def example():
   
   from matplotlib import pyplot as plt
   import cv2
   im_file =exec_folder+'/wrench.bmp'
   image=cv2.imread(im_file)# the scipy.misc.imread uses PIL which give an error for this bmp file (Unsupported BMP compression )
   output,animation=chanvese(image)
   plt.ion()
   for frame in  animation:
      plt.imshow(frame)
      plt.draw()
      plt.show()
   plt.ioff()
   plt.imshow(output, cmap='Greys_r')
   plt.show()
   print 'done' 
   
if __name__ == '__main__':
   import sys 
   if 'install' in sys.argv:
      _install()
   else:
      example()




