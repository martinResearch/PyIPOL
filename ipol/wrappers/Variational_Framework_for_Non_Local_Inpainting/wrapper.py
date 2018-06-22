import tempfile   
import os
from imageio import imwrite,imread
import ipol.tools as tools
import subprocess
import glob
from subprocess import Popen, PIPE, STDOUT



string="""Variational Framework for Non-Local Inpainting
Vadim Fedorov, Gabriele Facciolo, Pablo Arias
http://www.ipol.im/pub/art/2015/136/"""

exec_folder=tools.extraction_directory+'/inpaint_9'
source_directory=exec_folder


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
   imwrite(image_file,image)
   mask_file =tempfile.mkstemp('.PNG')[1]
   imwrite(mask_file,mask)

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






