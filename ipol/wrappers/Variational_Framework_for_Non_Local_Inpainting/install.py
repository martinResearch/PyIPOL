import tempfile   
import os
from imageio import imwrite,imread
import  tools
import subprocess
import glob
from subprocess import Popen, PIPE, STDOUT



string="""Variational Framework for Non-Local Inpainting
Vadim Fedorov, Gabriele Facciolo, Pablo Arias
http://www.ipol.im/pub/art/2015/136/"""

exec_folder=tools.extraction_directory+'/inpaint_9'
source_directory=exec_folder
def _install():
   """this function downloads and compile the code for the inpainting implementation"""
   download_file='http://www.ipol.im/pub/art/2015/136/inpaint_8.tgz'
   tools.download_and_extract(download_file)  
   this_file_path=os.path.dirname(__file__)
   subprocess.call(' mkdir build; cd build; cmake ..; make', shell=True,cwd=exec_folder)   
  
   

