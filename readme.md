# Project's goals

The goal of this project is to provide an easy-to-install set of python bindings around the image processing and computer vision C++
code from *Image Processing On Line* [IPOL](http://www.ipol.im/)

 
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
	* A Review of Classic Edge Detectors
	* LSD: a Line Segment Detector

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

or 
	import ipol 
	import os
	print os.listdir(os.path.join(ipol.path,'examples'))


