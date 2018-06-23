import tempfile   
import os
from imageio import imwrite,imread
import tools
import subprocess


string="""Implementation of the "Non-Local Bayes" (NL-Bayes) Image Denoising Algorithm
Marc Lebrun, Antoni Buades, Jean-Michel Morel"""

path=os.path.dirname(__file__)

exec_folder=tools.extraction_directory+'/nl-bayes_20130617'
source_directory=exec_folder
def _install():
   """this function downloads and compile the code for the chanvese implementation"""
   download_file='http://www.ipol.im/pub/art/2013/16/nl-bayes_20130617.zip'
   tools.download_and_extract(download_file)  
   # getting example images

   subprocess.call('make OMP=1', shell=True,cwd=exec_folder)   
   
   



