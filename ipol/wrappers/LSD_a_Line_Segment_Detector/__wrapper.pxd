# distutils: language = c++


cdef extern from "../../csources/lsd_1.6/lsd.h":
	double * lsd(int * n_out, double * img, int X, int Y)


