import os
import tools
import subprocess


string="""Rudin-Osher-Fatemi Total Variation Denoising using Split Bregman. Pascal Getreuer"""

path=os.path.dirname(__file__)

exec_folder=tools.extraction_directory+'/tvdenoise_20120516'
source_directory=exec_folder
def _install():
   """this function downloads and compile the code for the chanvese implementation"""
   download_file='http://www.ipol.im/pub/art/2012/g-tvd/tvdenoise_20120516.tar.gz'
   tools.download_and_extract(download_file)  
   os.system( 'sudo apt-get install build-essential libjpeg8-dev libpng-dev libtiff-dev')
   this_file_path=os.path.dirname(__file__)
   subprocess.call('make -f makefile.gcc', shell=True,cwd=exec_folder)   
   
   
