#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tempfile   
import os
from imageio import imwrite,imread
from skimage.io import imread as skimage_imread
import ipol.tools as tools
import subprocess
import shutil
import numpy as np
# todo: replace the followin string  by the name of the folder in the zip file
zip_subfolder='sms_optic_flow_2.0'
source_directory=os.path.join(tools.extraction_directory,zip_subfolder) 
binary_directory1=os.path.join(tools.extraction_directory,zip_subfolder,'spatial') 
binary_directory2=os.path.join(tools.extraction_directory,zip_subfolder,'temporal') 


string="""Robust Optical Flow Estimation
Javier Sánchez Pérez, Nelson Monzón López, Agustín Salgado de la Nuez""" # todo: put the name of the paper you are adding to PyIPOL

path=os.path.dirname(__file__)



def temporal( Images,  alpha=18, gamma=1, nscales=100, zoom_factor=0.75, TOL=0.0001, inner_iter=1, outer_iter=15,verbose=False):
   """
   Enhance the colors of an image using the method decribed in    
      Automatic Color Enhancement (ACE) and its Fast Implementation
      Pascal Getreuer IPOL 2012
      
   Usage: 
   inputs 

	Images      : list of images as a list of numpy arrays 
	processors  : number of processors to run the method
	alpha       : weight of the smoothing term
	gamma       : weight of the gradient constancy term
	nscales     : desired number of scales
	zoom_factor : downsampling factor 
	TOL         : stopping criterion threshold for the numerical scheme
	inner_iter  : number of inner iterations in the numerical scheme
	outer_iter  : number of outer iterations in the numerical scheme	
	verbose     : 0 or 1, for quiet or verbose behaviour
   return 
      	list of optical flow images as numpy arrays
   """   
   # todo : you can copy the documentation from the C++ file
   # it is prefered to clean the description for it to better 
   # reflect the python binding interface
  
   #  create temporary folder where temporary file while be read an created by the executable
   tmp_folder=tempfile.mkdtemp()
   if not (isinstance([],list)):
      BaseException('your input image should be pu in a python list')
   
   # todo : save the input images 
   listfiles=[]
   size=Images[0].shape
   for i,image in enumerate(Images):	
      assert(np.all(image.shape==size))
      filename='input%d.png'%i
      imwrite(os.path.join(tmp_folder,filename),image)
      listfiles.append(filename)	  
   listfilestr=' '.join(listfiles)
  
      
   command='cd %s'%tmp_folder+';'# moving in the temporary folder
   command+=os.path.join(binary_directory2,'main ')+' %d %s %f %f %d %f %f %d %d %s %d'%(len(Images),listfilestr,\
      alpha, gamma, nscales, zoom_factor, TOL, inner_iter, outer_iter,tmp_folder,verbose)
      
   # calling the executable
   os.system( command)   

   #todo: read the output from the temporary file
   flows=[]
   for i in range(len(Images)-1):
      output_file=os.path.join(tmp_folder,'flow%02d.uv'%i)
      with open(output_file,'r') as file:
         file.readline()
         file.readline()
         file.readline()  
         flows.append(np.fromfile(file,dtype=np.float32)[57:].reshape(2,size[0],size[1]).transpose((1,2,0)))

   shutil.rmtree(tmp_folder)

   return flows

def spatial( image1,image2, processors=1, alpha=18, gamma=1, nscales=100, zoom_factor=0.75, TOL=0.0001, inner_iter=1, outer_iter=15,verbose=False):
   """
   Enhance the colors of an image using the method decribed in    
      Automatic Color Enhancement (ACE) and its Fast Implementation
      Pascal Getreuer IPOL 2012
      
   Usage: 
   inputs 

	Images      : list of images as a list of numpy arrays 
	processors  : number of processors to run the method
	alpha       : weight of the smoothing term
	gamma       : weight of the gradient constancy term
	nscales     : desired number of scales
	zoom_factor : downsampling factor 
	TOL         : stopping criterion threshold for the numerical scheme
	inner_iter  : number of inner iterations in the numerical scheme
	outer_iter  : number of outer iterations in the numerical scheme	
	verbose     : 0 or 1, for quiet or verbose behaviour
   return 
      	list of optical flow images as numpy arrays
   """   
   # todo : you can copy the documentation from the C++ file
   # it is prefered to clean the description for it to better 
   # reflect the python binding interface
  
   #  create temporary folder where temporary file while be read an created by the executable
   tmp_folder=tempfile.mkdtemp()
   if not (isinstance([],list)):
      BaseException('your input image should be pu in a python list')
   
   # todo : save the input images 

   imwrite(os.path.join(tmp_folder,'image1.png'),image1)
   imwrite(os.path.join(tmp_folder,'image2.png'),image2)

   command='cd %s'%tmp_folder+';'# moving in the temporary folder
   command+=os.path.join(binary_directory1,'main ')+' image1.png image2.png flow.uv %f %f %d %f %f %d %d %s %d'%(\
      alpha, gamma, nscales, zoom_factor, TOL, inner_iter, outer_iter,tmp_folder,verbose)
      
   # calling the executable
   os.system( command)   

   #todo: read the output from the temporary file
   output_file=os.path.join(tmp_folder,'flow.uv')
   with open(output_file,'r') as file:
      file.readline()
      file.readline()
      file.readline()  
      flow=np.fromfile(file,dtype=np.float32)[57:].reshape(2,image1.shape[0],image1.shape[1]).transpose((1,2,0))

   # delete the temporary files
   shutil.rmtree(tmp_folder)

   return flow




