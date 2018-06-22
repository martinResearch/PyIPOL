import tempfile   
import os
from imageio import imwrite,imread
import tools
import subprocess

string="""Chan-Vese Segmentation 
Pascal Getreuer
http://www.ipol.im/pub/art/2012/g-cv"""

path=os.path.dirname(__file__)

exec_folder=tools.extraction_directory+'/chanvese_20120715'
source_directory=exec_folder

def _install():
   """this function downloads and compile the code for the chanvese implementation"""
   download_file='http://www.ipol.im/pub/art/2012/g-cv/chanvese_20120715.tar.gz'
   tools.download_and_extract(download_file)  
   this_file_path=os.path.dirname(__file__)
   subprocess.call('make -f makefile.gcc', shell=True,cwd=exec_folder)   
   
