import os
import tools
import subprocess


string="""Automatic Color Enhancement (ACE) and its Fast Implementation
Pascal Getreuer"""



exec_folder=tools.extraction_directory+'/ace_20121029'
source_directory=exec_folder
def _install():
   """this function downloads and compile the code for the chanvese implementation"""
   download_file='http://www.ipol.im/pub/art/2012/g-ace/ace_20121029.tar.gz'
   tools.download_and_extract(download_file) 
   subprocess.call('make -f makefile.gcc', shell=True,cwd=exec_folder)   
   
   

