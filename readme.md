# Project's goal

The goal of this project is to provide an easy-to-install set of python bindings around C++ implementations of image processing and computer vision algorithms from *Image Processing On Line* [IPOL](http://www.ipol.im/). 

IPOL is a great source of state-of-art algorithms in the domain of image processing and computer vision. For each accepted paper a demo is made available online which is very valuable as people can quickly test the algorithms without the need to install them on their own machines. However if one wants to reuse some of these algorithms as part of a larger project written in Python, there is still a non negligible cost associated with the process of downloading and compiling each individual code we want to test as well as writing the scripts that generate temporary input files, call the executable with the right arguments and load the results from the generated files. We aim at reducing that cost by proving a **pythonic interface to IPOL algorithms** through one-line installer.

The goal of the project **is not** to re-implement algorithm from IPOL in Python or Cython, but only to create interfaces with minimal modification of the original C++ code. 
The C++ code is not stored in this repository but downloaded during the installation and potential modifications on the C++ code are saved as patches. 
 
# Installation

## Linux

using pip

	sudo pip install git+git://github.com/martinResearch/PyIPOL.git


local installation 

	wget https://github.com/martinResearch/PyIPOL/archive/master.zip --no-check-certificate
	unzip master.zip 
	cd PyIPOL-master
	python setup.py build_ext --inplace
## Windows

the installation functions need to be modified to work on windows

## Mac OS

not tested yet

# Available bindings

we are using the same categorization as [IPOL](http://www.ipol.im/)



* Blur
	* Total Variation Deconvolution using Split Bregman [on IPOL](http://www.ipol.im/pub/art/2012/g-tvdc/)
 
* Color and Contrast
	* Automatic Color Enhancement (ACE) and its Fast Implementation [on IPOL](http://www.ipol.im/pub/art/2012/g-ace/)

* Denoising
	* Implementation of the "Non-Local Bayes" (NL-Bayes) Image Denoising Algorithm [on IPOL](http://www.ipol.im/pub/art/2013/16/)
	* Rudin-Osher-Fatemi Total Variation Denoising using Split Bregman [on IPOL](http://www.ipol.im/pub/art/2012/g-tvd/)
	* DCT Image Denoising: a Simple and Effective Image Denoising Algorithm [on IPOL](http://www.ipol.im/pub/art/2011/ys-dct/)
	* Non-Local Means Denoising [on IPOL](http://www.ipol.im/pub/art/2011/bcm_nlm/)

* Inpainting
	* Variational Framework for Non-Local Inpainting [on IPOL](http://www.ipol.im/pub/art/2015/136/)

* Optical Flow
	* TV-L1 Optical Flow Estimation [on IPOL](http://www.ipol.im/pub/art/2013/26/)

* Segmentation and Edges
	* A Review of Classic Edge Detectors [on IPOL](http://www.ipol.im/pub/art/2012/gjmr-lsd/)
	* Chan-Vese Segmentation [on IPOL](http://www.ipol.im/pub/art/2012/g-cv/)	
	* LSD: a Line Segment Detector [on IPOL](http://www.ipol.im/pub/art/2015/35/)

# Examples 


you can run an example directly from python 

 	import ipol.wrappers.Automatic_Color_Enhancement_and_its_Fast_Implementation.examples as ex
	ex.example()

you can find the example file and display the source of the example using 
	
	import ipol.wrappers.Automatic_Color_Enhancement_and_its_Fast_Implementation.examples as ex
	import inspect
	print inspect.getsourcefile(ex)
	print '------------------------------------'
	print inspect.getsource(ex)

you can run all the examples using

	import ipol.wrappers
	ipol.wrappers.run_all_examples()



# Related projects
* the IPOL in-browser demos can be downloaded an run locally using a local cherrypy based server and the code [here](https://githua matlb.com/carlodef/ipol_demo). Maybe that code could be used to help to write the python interfaces.
* Some Matlab interfaces to IPOL algorithms written by [Paul-Darius Sarmadi](http://sarmadi.fr/mex-ipol-library/) during a summer internship in 2014 are available [here](https://github.com/Paul-Darius/ipol-matlab). This project contains a report with guidelines to make IPOL code that can easily be interfaced with MATLAB.

# Limitations and possible improvements

* IPOL now  accepts Matlab code. We will have to call an octave interpreter from python.

* When the code has been written with files as input/outputs it might be difficult to create an nice python interface without modifying the code. Maybe using memory-mapped files could be a solution to avoid writing files to disk. However a direct interface without memory copies should be preferred when possible. (NOTE: the visible python interface must be independent to the underlying technique for the binding.  Thus, even if the algorithms are called internally by direct c/python bindings or using temporary files, the interface is *exactly* the same.  Designing this interface is an entirely independent task than implementeing it.  The interface is more important than the implementation, thus we may start by the simplest possible implementation). 
* As we do not store the C++ code in the repository, modifications in the compressed files on IPOL may break the bindings. We may need to store the IPOL codes in an other Git repository (or another branch?) to make things more robust.  (NOTE: this cannot happen, because the compressed files in ipol are frozen and will never change).
* We could provide some PyQt widgets and some python tools provide an user experience that is closer to the online interactive demos, with buttons and sliders to set up the parameters. (NOTE: ok, but this should be a separate project.  The python binding should be useful in a headless server without Qt libraries).



# troubleshooting


* if you get an error like ImportError: /usr/lib/python2.7/dist-packages/cv2.so: undefined symbol: _ZN2cv23adaptiveBilateralFilterERKNS_11_InputArrayERKNS_12_OutputArrayENS_5Size_IiEEddNS_6Point_IiEEi
you can start python as a super user.

*  if you get errors with *Permission denied* when running examples you may need to run python in super user mode. I am not sure how to change the permission of the files during the installation in order to avoid that 


# Contributing

It might be a good idea to start with the most cited IPOL articles [see here](https://scholar.google.fr/citations?user=LFdvV4YAAAAJ)



## Wrapping the executable 
The easiest way to create interface to some IPOL code is to call an executable with temporary files.


* get a copy of the repository 

		git clone https://github.com/martinResearch/PyIPOL.git


* copy one of the existing wrapper  PyIPOL/wrappers that does not use cython (no pxd and pyx files)

* move all the other wrappers in a different folder such that the folder wrapper contain only the new wrapper, which will speedup subsequent tests
	
 
* modify the  content of the files in order to put the right zip file url etc. 


* test the installation

		PyIPOL$ sudo setup.py install

* test the PyIPOL installation locally and the examples without beeing in th PyIPOL folder (in order to test the version that is copied in /usr/local/lib/python2.7/dist-packages/ and check that nothing breaks because of wrong relative paths)

		
	 	path/PyIPOL$ cd ..
		path$  python
		>>> import ipol
		>>> import ipol.wrappers.my_wrapper_name.examples as ex
		>>> ex.example()
	 
maybe this process could be further accelerated reusing the online demos python codes available [here](http://dev.ipol.im/git/?p=colom/ipol_demo.git;a=summary). 

## Using Cython

follow the same methodology as in the previous section but copy one of the existing wrapper PyIPOL/wrappers that uses cython (with pxd and pyx files)



## TODOS

* delete temporary files when not needed anymore

* improve the modules intialization files to get a better autocompletion in wingide or ipython

* improve the autocompletion for function wrapped with cython

* put the cython code in separated cython files for each paper 

* may put the python code for each paper in a sperate folder

## Guidelines for IPOL code

* **provide an executable that performs the task without access to the ground truth**: In some cases the executable does not provide enough control to a usefull access to the functionalty of the method.For example the code for [BM3D](http://www.ipol.im/pub/art/2012/l-bm3d/article_lr.pdf) does not provide an executable that take a noisy image as an input and denoise it. Instead it take an image that is not noisy, add some noise to it and compute denoising performance measures. While it is usefull for research purpose, it is useless from a pratical point of view. 

* **take temporary folder as input**: if your executable generates files without giving control of the names to the user, make it possible for the user to specify a folder where these files will be generated (example  measures.txt generated by the NL-bayes denoising method). We can use a trick for now which consist in moving in a temporary folder before calling the executable but this seems not very elegant.

* **seperate algorithm from file I/O**: this will make cython binding easier to code by avoifing the need of patching the C++ code. This is standard good practice in programming.






