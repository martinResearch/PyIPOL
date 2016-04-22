#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile   
import os
import tools
import subprocess
import numpy as np

string="""TV-L1 Optical Flow Estimation
Javier Sánchez Pérez, Enric Meinhardt-Llopis, Gabriele Facciolo"""

path=os.path.dirname(__file__)

exec_folder=tools.extraction_directory+'/tvl1flow_3'
source_directory=exec_folder

def _install():
   """this function downloads and compile the code """
   download_file='http://www.ipol.im/pub/art/2013/26/tvl1flow_3.tar.gz'
   tools.download_and_extract(download_file)  
   os.system( 'sudo apt-get install build-essential libjpeg8-dev libpng-dev libtiff-dev')
   this_file_path=os.path.dirname(__file__)
   subprocess.call('make', shell=True,cwd=exec_folder)   
   
   
