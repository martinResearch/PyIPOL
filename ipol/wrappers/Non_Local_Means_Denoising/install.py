import tempfile   
import os
from scipy.misc import imsave,imread
from skimage.io import imread as skimage_imread
import tools
import subprocess


string="""Non-Local Means Denoising
Antoni Buades, Bartomeu Coll, Jean-Michel Morel"""

path=os.path.dirname(__file__)

exec_folder=tools.extraction_directory+'/nlmeansC'
source_directory=exec_folder
def _install():
   """this function downloads and compile the code for the chanvese implementation"""
   download_file='http://www.ipol.im/pub/art/2011/bcm_nlm/nlmeansC.tar.gz'
   tools.download_and_extract(download_file)  
   import urllib
   # getting example images
   urllib.urlretrieve('http://www.ipol.im/pub/art/2011/bcm_nlm/cinput.jpg',os.path.join(exec_folder,'cinput.jpg'))
   urllib.urlretrieve('http://www.ipol.im/pub/art/2011/bcm_nlm/cnoisy.jpg',os.path.join(exec_folder,'cnoisy.jpg'))
   this_file_path=os.path.dirname(__file__)
   subprocess.call('make', shell=True,cwd=exec_folder)   
   
   



