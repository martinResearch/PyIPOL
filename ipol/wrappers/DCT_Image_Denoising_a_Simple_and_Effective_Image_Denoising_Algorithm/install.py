  
import os
import tools
import subprocess


string="""DCT Image Denoising: a Simple and Effective Image Denoising Algorithm
Guoshen Yu, Guillermo Sapiro"""

path=os.path.dirname(__file__)

exec_folder=tools.extraction_directory+'/src_demoDCTdenoising'
source_directory=exec_folder
def _install():
   """this function downloads and compile the code for the chanvese implementation"""
   download_file='http://www.ipol.im/pub/art/2011/ys-dct/src_demoDCTdenoising.tar.gz'
   tools.download_and_extract(download_file)  
   import urllib
   # getting example images
   urllib.urlretrieve('http://www.ipol.im/pub/art/2011/bcm_nlm/cinput.jpg',os.path.join(exec_folder,'cinput.jpg'))
   urllib.urlretrieve('http://www.ipol.im/pub/art/2011/bcm_nlm/cnoisy.jpg',os.path.join(exec_folder,'cnoisy.jpg'))
   
   subprocess.call('make OMP=1', shell=True,cwd=exec_folder)   
   
   
