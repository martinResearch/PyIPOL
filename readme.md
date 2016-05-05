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

**the installation functions need to be modified to work on windows**

The first steps could be:
* install Git from [here](https://git-scm.com/download/win)
* install MinGW + MSYS  from [here](https://sourceforge.net/projects/mingw/files/Installer/)(mingw32-base,mingw32-gcc-g++) 
* install Microsoft Visual Studio Express [here]()
* try nmake in command line ? 
* try make in command in MSYS terminal  ? 

	pip install git+git://github.com/martinResearch/PyIPOL.git
	
Using only cython bindingsmay help to avoid the need to install visual studio express or MinGW ? 

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
	
* Image comparison
	* An Analysis of the SURF Method [on IPOL](http://www.ipol.im/pub/art/2015/69/)
	* ASIFT: An Algorithm for Fully Affine Invariant Comparison [on IPOL](http://www.ipol.im/pub/art/2011/my-asift/)
	
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

* When the code has been written with files as input/outputs it might be difficult to create an nice python interface without modifying the code. Maybe using memory-mapped files could be a solution to avoid writing files to disk. However a direct interface without memory copies should be preferred when possible. (NOTE: the visible python interface must be independent of the underlying technique for the binding.  Thus, even if the algorithms are called internally by direct c/python bindings or using temporary files, the interface is *exactly* the same.  Designing this interface is an entirely independent task than implementeing it.  The interface is more important than the implementation, thus we may start by the simplest possible implementation).

* As we do not store the C++ code in the repository, modifications in the compressed files on IPOL may break the bindings. We may need to store the IPOL codes in an other Git repository (or another branch?) to make things more robust.  (NOTE: this cannot happen, because the compressed files in ipol are frozen and will never change).

* We could provide some PyQt widgets and some python tools provide a user experience that is closer to the online interactive demos, with buttons and sliders to set up the parameters. (NOTE: ok, but this should be a separate project.  The python binding should be useful in a headless server without Qt libraries).

* we can add an options to use a folder mounted in the RAM in order for the executables to read an write in RAM, for example using [this](https://gist.github.com/jcayzac/1231182) or  [this](http://stackoverflow.com/questions/4351048/how-can-i-create-a-ramdisk-in-python) on linux. But it might be difficult to make this system cross platform. On windows, one option could be to use [ImDisk](http://imdisk.en.lo4d.com/)

# troubleshooting


* if you get an error like ImportError: /usr/lib/python2.7/dist-packages/cv2.so: undefined symbol: _ZN2cv23adaptiveBilateralFilterERKNS_11_InputArrayERKNS_12_OutputArrayENS_5Size_IiEEddNS_6Point_IiEEi
you can start python as a super user.

*  if you get errors with *Permission denied* when running examples you may need to run python in super user mode. I am not sure how to change the permission of the files during the installation in order to avoid that 


# Contributing

It might be a good idea to start with the most cited IPOL articles [see here](https://scholar.google.fr/citations?user=LFdvV4YAAAAJ)



### Wrapping an executable 
The easiest way to create interface to some IPOL code is to call an executable with temporary files.

* fork the project on github

* get a local copy of the repository 

		git clone https://github.com/yourUserName/PyIPOL.git



* make a copy of the folder  PyIPOL/new_wrappers/new_paper_example in PyIPOL/new_wrappers and rename it with the name of the paper you are adding, replacing spaces by underscore and removing special characters 
	
	 	cd PyIPOL/new_wrapper
	 	cp new_wrapper_example name_of_you_paper_with_underscores

* with the new folder, modify the  content of the file *install.py* 
	* change the url of the zip file containing the c++ code for that paper 
	* look at the name of the folder within the zip file and modify the end of the line that set up the variable *zip_subfolder* in order to point to that folder after decompression of the zip file
	* change the compilation line if needed (often *make -f makefile.gcc*, look at the readme in the source zip file for that paper)

* test the installation in place

		PyIPOL/new_wrappers$ python test_install.py 

	you should have the source code and the compiled executable in a subfolder of *PyIPOL/ipol/csources*
		
* edit *example.py* by replacing the string *new_paper_name* by the name of the name of the paper you are adding with the underscores.
* modify the content of *wrapper.py* by changing the name of the function , the list of its argument, and calling the executable with the right set of arguments and temporary file names.
* modify *examples.py* to test the new wrapper and test it until it works using the following line:
		
		PyIPOL/new_wrappers$ python test_wrapper.py

* edit *example.py* by replacing the string *new_wrappers* by *wrappers* and move your new wrapper into the folder *PyIPOL/wrappers*.

* test the PyIPOL installation and the examples without being in th PyIPOL folder (in order to test the version that is copied in /usr/local/lib/python2.7/dist-packages/ and check that nothing breaks because of wrong relative paths)

		path/PyIPOL$ sudo python setup.py install
	 	path/PyIPOL$ cd ..
		path$  python
		>>> import ipol
		>>> import ipol.wrappers.my_wrapper_name.examples as ex
		>>> ex.example()
		
* add the paper in the list of bindings in the readme.md file
		
* if that works, push on github and try to reinstall ipol from your repo and run all the examples
	sudo pip unsintall ipol
	sudo pip install git+git://github.com/yourGithubUserName/PyIPOL.git
	sudo python
	import ipol.wrappers
	ipol.wrappers.run_all_examples()

* if that works make a pull request on github. Thank you !

### Using Cython

follow the same methodology as in the previous section, but copy one of the existing wrapper PyIPOL/wrappers that uses cython (with pxd and pyx files) 



## TODOS

* delete temporary files when not needed anymore
* improve the module initialization files to get a better autocompletion in wingide or ipython
* improve the autocompletion for function wrapped with cython
* put the cython code in separate cython files for each paper 
* may put the python code for each paper in a seperate folder

## Guidelines for IPOL code

* **provide an executable that performs the task without access to the ground truth**: In some cases the executable does not provide a direct access to the method. For example the code for [BM3D](http://www.ipol.im/pub/art/2012/l-bm3d) does not provide an executable that takes a noisy image as an input and denoise it. Instead, it takes a ground truth image that isn't noisy, add some noise to it and compares the denoised image with the ground truth image. While it is useful for research purpose, it is useless from a practical point of view because in practice we do not have access to the ground truth when we want to denoise an image. 

* **take temporary folder as input**: if your executable generates files without giving control of the names to the user, make it possible for the user to specify a folder where these files will be generated (example  measures.txt generated by the NL-bayes denoising method). We can use a trick for now which consists in moving in a temporary folder before calling the executable, but this is not very elegant.

* **separate the algorithm implementation from file I/O and options parsing**: this will make the cython binding easier to code by avoiding the need of patching the C++ code. This is a standard of good practice in programming and it is already given as a recommendation in the IPOL software guidelines, in section 4.3:c.






