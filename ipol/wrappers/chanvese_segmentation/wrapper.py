import tempfile   
import os
from imageio import imwrite,imread
import ipol.tools as tools
import subprocess


string="""Chan-Vese Segmentation 
Pascal Getreuer
http://www.ipol.im/pub/art/2012/g-cv"""

path=os.path.dirname(__file__)

exec_folder=tools.extraction_directory+'/chanvese_20120715'
source_directory=exec_folder


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
   output_file=tempfile.mkstemp('.PNG')[1] 
   animation_file=tempfile.mkstemp('.gif')[1]
   temp_image_file =tempfile.mkstemp('.PNG')[1]
   imwrite(temp_image_file,image)

   if not phi0 is None:
      temp_phi0_file
      imwrite(temp_phi0_file,phi0)
      command=exec_folder+'/chanvese mu:%f nu:%f lambda1:%f lambda2:%f phi0:%s tol:%f maxiter:%d dt:%f iterperframe:%d %s %s %s'%(mu,nu,lambda1,lambda2,temp_phi0_file,tol,maxiter,dt,iterperframe,temp_image_file,animation_file,output_file)
   else:
      command=exec_folder+'/chanvese mu:%f nu:%f lambda1:%f lambda2:%f tol:%f maxiter:%d dt:%f iterperframe:%d %s %s %s'%(mu,nu,lambda1,lambda2,tol,maxiter,dt,iterperframe,temp_image_file,animation_file,output_file)
      
   # calling the executable
   os.system( command)
   
   #reading the output from the temporary file
   output=imread(output_file)
   os.remove(output_file)
   os.remove(temp_image_file)
   if getAnimation:
      animation=tools.read_animated_gif(animation_file)
      
      os.remove(animation_file)
      return output,animation
   else:
      return output


   
if __name__ == '__main__':
   import sys 
   if 'install' in sys.argv:
      _install()



