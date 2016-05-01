import tempfile   
import os
from scipy.misc import imsave,imread
from skimage.io import imread as skimage_imread
import ipol.tools as tools
import subprocess
import shutil
import numpy as np

# todo: replace the followin string  by the name of the folder in the zip file
zip_subfolder='demo_ASIFT_src'
source_directory=os.path.join(tools.extraction_directory,zip_subfolder) 


string="""ASIFT: An Algorithm for Fully Affine Invariant Comparison""" # todo: put the name of the paper you are adding to PyIPOL

path=os.path.dirname(__file__)


def asift(image1,image2,resize_input=0):# todo change the name of the function

   """
        *******************************************************************************
	***************************  ASIFT image matching  **************************** 
	******************************************************************************* 
	Usage: " << argv[0] << " imgIn1.png imgIn2.png imgOutVert.png imgOutHori.png  
	matchings.txt keys1.txt keys2.txt [Resize option: 0/1] 
	- imgIn1.png, imgIn2.png: input images (in PNG format). 
	- imgOutVert.png, imgOutHori.png: output images (vertical/horizontal concatenated, 
	  in PNG format.) The detected matchings are connected by write lines.
	- matchings.txt: coordinates of matched points (col1, row1, col2, row2). 
	- keys1.txt keys2.txt: ASIFT keypoints of the two images.
	- [optional 0/1]. 1: input images resize to 800x600 (default). 0: no resize. 
   	******************************************************************************* 
	*********************  Jean-Michel Morel, Guoshen Yu, 2010 ******************** 
	******************************************************************************* 

   """# todo : copy the documentation from the C++ file
  
 
   # save input images 
   tmp_folder=tempfile.mkdtemp()
   imsave(os.path.join(tmp_folder,'imgIn1.png'),image1)
   imsave(os.path.join(tmp_folder,'imgIn2.png'),image2)

   command='cd %s'%tmp_folder+';'# moving in the temporary folder
   command+=source_directory+'/demo_ASIFT imgIn1.png imgIn2.png imgOutVert.png imgOutHori.png matchings.txt keys1.txt keys2.txt %d'%resize_input
   

   # calling the executable
   os.system( command)   

   # todo: read the outputs from the temporary file
   # it call help to open the temporary folder in your file explorer
   #imgOutVert=imread(os.path.join(tmp_folder,'imgOutVert.png'))
   #imgOutHori=imread(os.path.join(tmp_folder,'imgOutHori.png'))

   with open(os.path.join(tmp_folder,'matchings.txt'),'r') as file:
      nbmatches=int(file.readline())#skipping the first line
      matchings=np.loadtxt(file)
      
   with open(os.path.join(tmp_folder,'keys1.txt'),'r') as file:
      file.readline()#skipping the first line that contain the size of the matrix
      keys1=np.loadtxt(file)     
      
   with open(os.path.join(tmp_folder,'keys2.txt'),'r') as file:
      file.readline()#skipping the first line that contain the size of the matrix
      keys2=np.loadtxt(file)
            
   # todo : delete the temporary files
   shutil.rmtree(tmp_folder)

   return matchings,keys1,keys2




