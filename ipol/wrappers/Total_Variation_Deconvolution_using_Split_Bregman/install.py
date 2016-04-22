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
source_directory=exec_folder
def _install():
   """this function downloads and compile the code for the tvdeconv implementation"""
   download_file='http://www.ipol.im/pub/art/2012/g-tvdc/tvdeconv_20120607.tar.gz'
   tools.download_and_extract(download_file)  
   this_file_path=os.path.dirname(__file__)
   subprocess.call('make -f makefile.gcc', shell=True,cwd=exec_folder)   
  
   



