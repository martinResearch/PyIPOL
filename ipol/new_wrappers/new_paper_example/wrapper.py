#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tempfile   
import os
from scipy.misc import imsave,imread
from skimage.io import imread as skimage_imread
import ipol.tools as tools
import subprocess
import shutil

# todo: replace the followin string  by the name of the folder in the zip file
zip_subfolder='ace_20121029'
source_directory=os.path.join(tools.extraction_directory,zip_subfolder) 


string="""Automatic Color Enhancement (ACE) and its Fast Implementation
Pascal Getreuer""" # todo: put the name of the paper you are adding to PyIPOL

path=os.path.dirname(__file__)


def ace(image,alpha,omega,sigma=None,method='interp',levels=None,degree=None,jpeg_quality=100):
   # todo change the name of the function and the list of arguments 

   """
   Enhance the colors of an image using the method decribed in    
      Automatic Color Enhancement (ACE) and its Fast Implementation
      Pascal Getreuer IPOL 2012
      
   Usage: 
   inputs 
      image <numpy array MxNx3>
                      the image you want to enhance
      alpha <number>  
                      stronger implies stronger enhancement
      omega <string>  
                      spatial weighting function, choices are
                      1/r      default ACE, omega(x,y) = 1/sqrt(x^2+y^2)
                      1        constant, omega(x,y) = 1
                      G        Gaussian
      sigma <float>   
                      sigma of the gaussian if omega=='G'
      method<string>  optional
                      method to use for fast computation, choices are
                      'interp' interpolate s_a(L - I(x)) with # levels
                      'poly'  polynomial s_a with degree #
                      default = 'interp'
      levels <number> 
                      number of levels if you use method=='interp'
      degree <number> 
                      number of degrees if you use method=='poly',
      jpeg_quality <number in 0-100> 
                     quality for saving the temporary JPEG images (0 to 100)
                     default=100
   return 
      output : the enhanced image as a numpy array
   """   
   # todo : you can copy the documentation from the C++ file
   # it is prefered to clean the description for it to better 
   # reflect the python binding interface
  
   #  create temporary folder where temporary file while be read an created by the executable
   tmp_folder=tempfile.mkdtemp()
   
   # todo : save the input images 
   imsave(os.path.join(tmp_folder,'input.png'),image)  

  
   # todo : generate the command to execute the executable with the right options
   if method=='interp':
      method_str='interp:%d'%levels
      assert(degree is None)
   elif ethod=='poly':
      method_str='poly:%d'%degree
      assert(levels is None)
   if omega=='G':
      omega_str='G %f'%sigma
   else:
      omega_str=omega
      assert(sigma is None)
      
   command='cd %s'%tmp_folder+';'# moving in the temporary folder
   command+=source_directory+'/ace -a %f -w %s -m %s input.png output.png'%(alpha,omega_str,method_str)
      
   # calling the executable
   os.system( command)   

   #todo: read the output from the temporary file
   output=imread(os.path.join(tmp_folder,'output.png'))  
   
   # if you have output as text file continaing matrices you can use 
   # the function loadtxt from numpy
   # example from  ASIFT_An_Algorithm_for_Fully_Affine_Invariant_Comparison:
   #    with open(os.path.join(tmp_folder,'matchings.txt'),'r') as file:
   #       nbmatches=int(file.readline())#skipping the first line
   #       matchings=np.loadtxt(file)
   
   # if you have output binary file continaing matrices you can use 
   # the function fromfile from numpy 
   # example from TV_L1_Optical_Flow_Estimation
   #   flow=np.fromfile(output_file,dtype=np.float32)[3:].reshape(image1.shape[0],image1.shape[1],2)
   
   # delete the temporary files
   shutil.rmtree(tmp_folder)

   return output




