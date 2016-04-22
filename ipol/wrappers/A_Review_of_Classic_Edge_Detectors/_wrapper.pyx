#experimental binding to IPOL algorithms written in cython
# distutils: language = c



cimport __wrapper
#cimport _cipol


import numpy as np
cimport numpy as np

from libc.stdlib cimport free
from cpython cimport PyObject, Py_INCREF
np.import_array()
from libcpp cimport bool


cdef class ArrayWrapper:
	""" Small Cython file to demonstrate the use of PyArray_SimpleNewFromData
	in Cython to create an array from already allocated memory.	
	Cython enables mixing C-level calls and Python-level calls in the same
	file with a Python-like syntax and easy type cohersion. See 
	http://cython.org for more information
	"""	
	# Author: Gael Varoquaux
	# License: BSD
	cdef void* data_ptr
	cdef int size
	cdef np.type dtype
	cdef set_data(self, int size, void* data_ptr,dtype=None):
		""" Set the data of the array
	
		This cannot be done in the constructor as it must recieve C-level
		arguments.
	
		Parameters:
		-----------
		size: int
		Length of the array.
		data_ptr: void*
		Pointer to the data            
	
		"""
		self.data_ptr = data_ptr
		self.size = size
		self.dtype=dtype
		
	
	def __array__(self):
		""" Here we use the __array__ method, that is called when numpy
		tries to get an array from the object."""
		cdef np.npy_intp shape[1]
		shape[0] = <np.npy_intp> self.size
		# Create a 1D array, of length 'size'
		if self.dtype==np.float32: # find enumerated type here http://docs.scipy.org/doc/numpy/user/c-info.how-to-extend.html
			ndarray = np.PyArray_SimpleNewFromData(1, shape,np.NPY_FLOAT32,  self.data_ptr)
		elif self.dtype==np.double:
			ndarray = np.PyArray_SimpleNewFromData(1, shape,np.NPY_FLOAT64,  self.data_ptr)
		else:
			print 'type not handled yet'
			raise
		return ndarray
	
	def __dealloc__(self):
		""" Frees the array. This is called by Python when all the
		references to the object are gone. """
		free(<void*>self.data_ptr)
	
cdef convertToNumpyWithoutCopy(void* coutput,shape,dtype):
	array_wrapper = ArrayWrapper()
	array_wrapper.set_data(np.prod(shape), <void*> coutput,dtype=dtype) 
	cdef np.ndarray output
	output = np.array(array_wrapper, copy=False).reshape(shape)
	output.base = <PyObject*> array_wrapper	
	#output.shape=image_c.shape
	Py_INCREF(array_wrapper)
	return output








def  edges_roberts(image,float threshold, int padding_method):	
	assert(image.ndim==2)
	cdef np.ndarray[np.float32_t, mode="c"] image_c= np.ascontiguousarray(image.flatten(), dtype=np.float32)		
	cdef float* coutput	
	coutput=__wrapper.edges_roberts(<float*>image_c.data,image.shape[1],image.shape[0],threshold,padding_method)
	output=convertToNumpyWithoutCopy(coutput,image.shape,np.float32)
	return output
	
def  edges_prewitt(image,float threshold, int padding_method):	
	assert(image.ndim==2)
	cdef np.ndarray[np.float32_t, mode="c"] image_c= np.ascontiguousarray(image.flatten(), dtype=np.float32)		
	cdef float* coutput	
	coutput=__wrapper.edges_prewitt(<float*>image_c.data,image.shape[1],image.shape[0],threshold,padding_method)
	output=convertToNumpyWithoutCopy(coutput,image.shape,np.float32)
	return output
	
def  edges_sobel(image,float threshold, int padding_method):	
	assert(image.ndim==2)
	cdef np.ndarray[np.float32_t, mode="c"] image_c= np.ascontiguousarray(image.flatten(), dtype=np.float32)		
	cdef float* coutput	
	coutput=__wrapper.edges_sobel(<float*>image_c.data,image.shape[1],image.shape[0],threshold,padding_method)
	output=convertToNumpyWithoutCopy(coutput,image.shape,np.float32)
	return output
	
def  edges_mh(image,float sigma, int n, float tzc, int padding_method):	
	assert(image.ndim==2)
	cdef np.ndarray[np.float32_t, mode="c"] image_c= np.ascontiguousarray(image.flatten(), dtype=np.float32)		
	cdef float* coutput	
	coutput=__wrapper.edges_mh(<float*>image_c.data,image.shape[1],image.shape[0],sigma,n,tzc,padding_method)
	output=convertToNumpyWithoutCopy(coutput,image.shape,np.float32)
	return output
	
def  edges_mh_log(image,float sigma, int n, float tzc, int padding_method):		
	assert(image.ndim==2)
	cdef np.ndarray[np.float32_t, mode="c"] image_c= np.ascontiguousarray(image.flatten(), dtype=np.float32)		
	cdef float* coutput	
	coutput=__wrapper.edges_mh_log(<float*>image_c.data,image.shape[1],image.shape[0],sigma,n,tzc,padding_method)
	output=convertToNumpyWithoutCopy(coutput,image.shape,np.float32)
	return output
	
	
def  edges_haralick(image, float rhozero, int padding_method):
	assert(image.ndim==2)
	cdef np.ndarray[np.float32_t, mode="c"] image_c= np.ascontiguousarray(image.flatten(), dtype=np.float32)		
	cdef float* coutput	
	coutput=__wrapper.edges_haralick(<float*>image_c.data,image.shape[1],image.shape[0],rhozero,padding_method)
	output=convertToNumpyWithoutCopy(coutput,image.shape,np.float32)
	return output
