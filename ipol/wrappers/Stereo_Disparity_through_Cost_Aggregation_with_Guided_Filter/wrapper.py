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
zip_subfolder='stereo-guided-filter_1.0'
source_directory=os.path.join(tools.extraction_directory,zip_subfolder) 
binary_directory=os.path.join(source_directory,'Build')

string=""" Stereo Disparity through Cost Aggregation with Guided Filter
Pauline Tan, Pascal Monasse """ # todo: put the name of the paper you are adding to PyIPOL

path=os.path.dirname(__file__)


def stereoGuidedFilter(image1,image2,dmin,dmax,R=9,A=0.9,E=6.5025,C=7,G=2,o=0,O='r',r=19,c=25.5,s=9):
   # todo change the name of the function and the list of arguments 

   """
	- Run
	Usage: ./stereoGuidedFilter [options] im1.png im2.png dmin dmax


	Inputs:
		image,image2: numpy arrays , input images
		Cost-volume filtering parameters:
		    R radius: radius of the guided filter (9)
		    A alpha: value of alpha (0.9)
		    E epsilon: regularization parameter (6.5025)
		    C tau1: max for color difference (7)
		    G tau2: max for gradient difference (2)

		Occlusion detection:
		    o tolDiffDisp: tolerance for left-right disp. diff. (0)

		Densification:
		    O sense: fill occlusion, sense='r':right,'l':left
		    r radius: radius of the weighted median filter (19)
		    c sigmac: value of sigma_color (25.5)
		    s sigmas: value of sigma_space (9)

		The parameter 'sense' used in densification is the direction of camera motion:
		     from left to right (value 'r'), common for Middlebury pairs
		     from right to left (value 'l')

	Output
		dictionnary with :
			disparity: disparity map after cost-volume filtering
			occlusion: after left-right check
			occlusion_filled: simple densification
			occlusion_filled_smoothed: final densification with median filter
   """   
   # todo : you can copy the documentation from the C++ file
   # it is prefered to clean the description for it to better 
   # reflect the python binding interface
  
   a=(dmax-dmin )# we do not provide these options to the user in the wrapper, as we want the exact disparities in the output
   b=0
  
   #  create temporary folder where temporary file while be read an created by the executable
   tmp_folder=tempfile.mkdtemp()
   
   # todo : save the input images 
   imsave(os.path.join(tmp_folder,'image1.png'),image1)  
   imsave(os.path.join(tmp_folder,'image2.png'),image2) 
  
   # todo : generate the command to execute the executable with the right options

   command='cd %s'%tmp_folder+';'# moving in the temporary folder
   command+=binary_directory+'/stereoGuidedFilter -R %d -A %g -E %g -C %g -G %g -o %d -O %s -r %d -c %g -s %d -a %d -b %d image1.png image2.png %d %d ' \
         %(R,A,E,C,G,o,O,r,c,s,a,b,dmin,dmax)
      
   # calling the executable
   os.system( command)   

   #todo: read the output from the temporary file
   disparity=imread(os.path.join(tmp_folder,'disparity.png'))[:,:,0]+dmin  
   disparity_occlusion=imread(os.path.join(tmp_folder,'disparity_occlusion.png'))[:,:,0]+dmin  
   disparity_occlusion_filled=imread(os.path.join(tmp_folder,'disparity_occlusion_filled.png'))[:,:,0] +dmin  
   disparity_occlusion_filled_smoothed=imread(os.path.join(tmp_folder,'disparity_occlusion_filled_smoothed.png'))[:,:,0] +dmin  
  
   shutil.rmtree(tmp_folder)

   return 	{'disparity':disparity,\
		'occlusion':disparity_occlusion,\
		'occlusion_filled':disparity_occlusion_filled,\
                'occlusion_filled_smoothed':disparity_occlusion_filled_smoothed}




