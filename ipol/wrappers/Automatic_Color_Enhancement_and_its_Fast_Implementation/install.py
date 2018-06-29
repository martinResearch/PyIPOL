import os
import tools
import subprocess
import platform
from shutil import copy
string="""Automatic Color Enhancement (ACE) and its Fast Implementation
Pascal Getreuer"""



exec_folder=os.path.join(tools.extraction_directory,'ace_20121029')
source_directory=exec_folder
def _install():
        """this function downloads and compile the code for the chanvese implementation"""
        download_file='http://www.ipol.im/pub/art/2012/g-ace/ace_20121029.tar.gz'
        tools.download_and_extract(download_file) 
        if platform.system()=="Windows":
                tools.download_and_extract('ftp://ftp.fftw.org/pub/fftw/fftw-3.3.5-dll32.zip') 
                path=os.path.dirname(__file__)
                #replacing the makefile.gcc file
                copy(os.path.join(path,'patch','makefile.gcc'), os.path.join(exec_folder,'makefile.gcc'))
                subprocess.call('make CC=gcc -f makefile.gcc', shell=True,cwd=exec_folder)  
                
        else:
                subprocess.call('make -f makefile.gcc', shell=True,cwd=exec_folder)   



