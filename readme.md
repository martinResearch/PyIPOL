# Project's goals

The goal of this project is to provide an easy-to-install set of python bindings around C++ implementations of image processing and computer vision algorithms from *Image Processing On Line* [IPOL](http://www.ipol.im/)

The goal of the project in not to reimplement algorithm from IPOL in python or Cython, but only to create interfaces with minimal modification of the original C++ code. 
The C++ code is not stored in this repository but downloaded duing the installation and modifications on the C++ code are saved as patches. 
 
# Installation

using pip

	sudo pip install git+git://github.com/martinResearch/PyIPOL.git


local installation 

	wget https://github.com/martinResearch/PyIPOL/archive/master.zip --no-check-certificate
	unzip master.zip 
	cd PyIPOL-master
	python setup.py build_ext --inplace


# Available Bindings

we are using the same categorization as [IPOL](http://www.ipol.im/)

* 3D
 
* SEGMENTATION AND EDGES
	* A Review of Classic Edge Detectors [on IPOL](http://www.ipol.im/pub/art/2012/gjmr-lsd/)
	* LSD: a Line Segment Detector [on IPOL](http://www.ipol.im/pub/art/2015/35/)

# Related projects
* the IPOL in-browser demos can be downloaded an run locally using a local cherrypy based server and the code [here](https://githua matlb.com/carlodef/ipol_demo). Maybe that code could be used to help to write the python interfaces.
* Some Matlab interfaces to IPOL algorithms written by [Paul-Darius Sarmadi](http://sarmadi.fr/mex-ipol-library/) during a summer internship in 2014 are available [here](https://github.com/Paul-Darius/ipol-matlab). This project contains a report with guidelines to make IPOL code easily interfacable with MATLAB.

# Limitations

* IPOL now *unfortunalty* accepts matlab code. Matlab code cannot easily be interfaced with python.
* When the code has been writen with files as input/ouputs it might be difficult to create an nice python interface without modifying the code. Maybe using memory-mapped files could be a solution to avoid writting files to disk.

# Examples 

Once installed examples can be found in 

	/usr/local/lib/python2.7/dist-packages/ipol/examples

If that is not the case you find where ipol has been installed from python using

	import ipol
	print ipol.path

you can lanch an example directly from within python using a simple import, for example for lsd: 

	import ipol.examples.test_lsd

you can get the list of examples as follows :

	import ipol.examples
	print ipol.examples.list

or using 

	import ipol 
	import os
	print os.listdir(os.path.join(ipol.path,'examples'))


