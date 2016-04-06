# distutils: language = c++
from libcpp cimport bool
cdef extern from "./csources/lsd_1.6/lsd.h":
	double * lsd(int * n_out, double * img, int X, int Y)

cdef extern from "./csources/classic_edge_detectors_1.0/classic_edge_detectors.h":
	float *edges_roberts(float *im, int w, int h,
		             float threshold, int padding_method)
	float *edges_prewitt(float *im, int w, int h,
		             float threshold, int padding_method)
	float *edges_sobel(float *im, int w, int h,
		           float threshold, int padding_method)
	float *edges_mh(float *im, int w, int h,
		        float sigma, int n, float tzc, int padding_method)
	float *edges_mh_log(float *im, int w, int h,
		            float sigma, int n, float tzc, int padding_method)
	float *edges_haralick(float *im, int w, int h,
		              float rhozero, int padding_method)



#cdef extern from "/media/veracrypt1/PyIPOL/ipol/csources/chanvese_20120715/chanvese.c":
#	int ChanVese(float *Phi, const float *f, int Width, int Height, int NumChannels, const chanveseopt *Opt);

