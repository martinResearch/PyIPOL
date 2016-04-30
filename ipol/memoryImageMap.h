// this files allows to create a dictionnary that map names to arrays in the memory 
// trought the use of a dictionnary.
// It exposes an interface with read/ read function that looks like
// reading and writing image from and to the hard drive but no file is actually created on the hard drive,
// file names are just keys of the dictionnary
// by including this header in the C++ code, and using a cython binding to add 
// data from python in that dictionnary, one can more easily pass data without making copies to 
// to a function that have been initially designed to work with image files instead of arrays in memory



struct MemoryImage{
 int height
 int width
 int nbChanels
 char * data_ptr
}

global  std::map<str,image  > nameToArrayMap;


write_png(const uint32_t *image, int width, int height, FILE *file)

void readMemoryImage(char *name,char *data_ptr, int width, int height,int nbChanels,bool copy)
{
	MemoryImage im=nameToArrayMap(name)
	width=im.width=;
	height=im.height=height;
	nbChanels=im.nbChanels=nbChanels;
	if copy
	{
		data_ptr=malloc()
		memcopy()
	}
	else{
		data_ptr=im.data_ptr;
	}
	
}

void writeMemoryImage(char *name,char *data_ptr, int width, int height,int nbChanels,bool copy)
{
	MemoryImage im;
	if copy
	{
		//need to allocate memory
		im.data_ptr=malloc()
		memcopy(data_ptr,im.data_ptr,)

	}
	else
	{
		im.data_ptr=data_ptr;
	}
	im.width=width;
	im.height=height;
	im.nbChanels=nbChanels;
	nameToArrayMap(name)=im;
	// need to make sur the data will not be freed
}



