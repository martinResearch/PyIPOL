import os
import subprocess
import tools


# todo: replace the followin string  by the name of the folder in the zip file
zip_subfolder='ace_20121029'
source_directory=os.path.join(tools.extraction_directory,zip_subfolder) 


def _install():
   
   """this function downloads and compile the code for the chanvese implementation"""
   download_file='http://www.ipol.im/pub/art/2012/g-ace/ace_20121029.tar.gz'
   tools.download_and_extract(download_file) 
   subprocess.call('make -f makefile.gcc', shell=True,cwd=source_directory)   
   
   

