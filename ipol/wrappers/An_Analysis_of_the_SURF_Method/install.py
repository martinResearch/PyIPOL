import os
import subprocess
import tools


# todo: replace the followin string  by the name of the folder in the zip file
zip_subfolder='demo_SURF_src'
source_directory=os.path.join(tools.extraction_directory,zip_subfolder) 


def _install():
   
   """this function downloads and compile the code for the SURF implementation"""
   download_file='http://www.ipol.im/pub/art/2015/69/demo_SURF_src.zip'
   tools.download_and_extract(download_file) 
   subprocess.call('make OMP=1', shell=True,cwd=source_directory)    
   
   

