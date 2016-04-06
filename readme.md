# Project's goals

The goal of this project is to provide an easy-to-install set of python bindings around C++ implementations of image processing and computer vision algorithms from *Image Processing On Line* [IPOL](http://www.ipol.im/)

 
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
* the IPOL in-browser demos can be downloaded an run locally using a local cherrypy based server and the code [here](https://github.com/carlodef/ipol_demo). Maybe that code could be used to help to write the python interfaces.
* Some Matlab interface to IPOL algorithms is available [here](https://github.com/Paul-Darius/ipol-matlab)



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


