import tempfile   
import os
from imageio import imwrite,imread
from skimage.io import imread as skimage_imread
import ipol.tools as tools
import subprocess
import shutil
import numpy as np

# todo: replace the followin string  by the name of the folder in the zip file
zip_subfolder='demo_SURF_src'
source_directory=os.path.join(tools.extraction_directory,zip_subfolder) 
bin_directory=os.path.join(source_directory,'bin')

string="""An Analysis of the SURF Method""" # todo: put the name of the paper you are adding to PyIPOL

path=os.path.dirname(__file__)


def extract_surf(image):# todo change the name of the function

   """********************************************************************* 

   """# todo : copy the documentation from the C++ file
  
 
   # save input images 
   tmp_folder=tempfile.mkdtemp()
   imwrite(os.path.join(tmp_folder,'image.png'),image)
  

   command='cd %s'%tmp_folder+';'# moving in the temporary folder
   command+=bin_directory+'/extract_surf image.png surf_point.txt'
   

   # calling the executable
   os.system( command)   

   # todo: read the outputs from the temporary file
   # it call help to open the temporary folder in your file explorer
   #imgOutVert=imread(os.path.join(tmp_folder,'imgOutVert.png'))
   #imgOutHori=imread(os.path.join(tmp_folder,'imgOutHori.png'))

   with open(os.path.join(tmp_folder,'surf_point.txt'),'r') as file:
      l=file.readline()#skipping the first line
      l=file.readline()
      key_points=np.loadtxt(file)


            
   # todo : delete the temporary files
   shutil.rmtree(tmp_folder)

   return key_points


def match_surf(surf_points1,surf_points2):# todo change the name of the function

   """********************************************************************* 

   """# todo : copy the documentation from the C++ file
  
   tmp_folder=tempfile.mkdtemp()
   with open(os.path.join(tmp_folder,'surf_point1.txt'),'w') as file:
      file.write('%d\n'%(surf_points1.shape[1]-5))
      file.write('%d\n'%surf_points1.shape[0])
      np.savetxt(file,surf_points1,fmt='%g')

   with open(os.path.join(tmp_folder,'surf_point2.txt'),'w') as file:
      file.write('%d\n'%(surf_points2.shape[1]-5))
      file.write('%d\n'%surf_points2.shape[0])
      np.savetxt(file,surf_points2,fmt='%g')

   command='cd %s'%tmp_folder+';'# moving in the temporary folder
   command+=bin_directory+'/match_surf surf_point1.txt surf_point2.txt matches.txt'
   

   # calling the executable
   os.system( command)   

   # todo: read the outputs from the temporary file
   # it call help to open the temporary folder in your file explorer
   #imgOutVert=imread(os.path.join(tmp_folder,'imgOutVert.png'))
   #imgOutHori=imread(os.path.join(tmp_folder,'imgOutHori.png'))

   with open(os.path.join(tmp_folder,'matches.txt'),'r') as file:
      file.readline()#skipping the first line
      matches=np.loadtxt(file)


            
   # todo : delete the temporary files
   shutil.rmtree(tmp_folder)

   return matches



