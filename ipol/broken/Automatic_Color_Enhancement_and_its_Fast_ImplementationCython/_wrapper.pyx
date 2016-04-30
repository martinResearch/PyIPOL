#experimental binding to IPOL algorithms written in cython
# distutils: language = c



cimport __wrapper 

from libc.stdlib cimport malloc, free


def main(args):
    cdef char **c_argv
    # make *sure* that we have the exact string object for every argument
    #, and don't invoke __str__ on something else!!
    args = [b'calling_from_cython'] + [bytes(x) for x in args]
    # or, use str(x).encode(...) above, depending on what API you want and what encoding C program expect
    c_argv = <char**>malloc(sizeof(char*) * len(args))
    for idx, s in enumerate(args):
        c_argv[idx] = s
    __wrapper.main(len(args), c_argv)
       

