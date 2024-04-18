To build the shared library run `gcc -fPIC -shared -o libtausworthe.so tausworthe.c tausworthe_wrapper.c`

Note that the tausworthe generator was implemented in C and called in python via a wrapper function because
even when using Ctypes module in Python I couldn't get the numbers generated numbers to match up when
comparing those produced by the python implementation and the c implementation.
