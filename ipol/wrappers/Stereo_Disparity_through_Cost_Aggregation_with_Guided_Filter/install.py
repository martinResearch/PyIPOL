#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import tools


# todo: replace the followin string  by the name of the folder in the zip file
zip_subfolder='stereo-guided-filter_1.0'
source_directory=os.path.join(tools.extraction_directory,zip_subfolder) 


def _install():
   """this function downloads and compiles the code"""

   # downloading and extraction the zip file 
   download_file='http://www.ipol.im/pub/art/2014/78/stereo-guided-filter_1.0.tar.gz' # todo: put the right zip file url
   tools.download_and_extract(download_file) 


   # getting example images 
   # if there are no eample images in the zip file we can get some exemple images from the demo page
   # tools.urlretrieve('http://www.ipol.im/pub/art/2011/bcm_nlm/cinput.jpg',os.path.join(exec_folder,'cinput.jpg'))
   # tools.urlretrieve('http://www.ipol.im/pub/art/2011/bcm_nlm/cnoisy.jpg',os.path.join(exec_folder,'cnoisy.jpg'))


   subprocess.call('mkdir Build && cd Build;cmake -D CMAKE_BUILD_TYPE:string=Release ..;make', shell=True,cwd=source_directory)   
   # an other compilation command example in case the is a MakeFile file
   # subprocess.call('make OMP=1', shell=True,cwd=source_directory) 
   
   

