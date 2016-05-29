CLIPOL: a command line interface to IPOL

All the implementation is contained on a single file "clipol.py", which is an
executable python script.  This code has two separate goals:

1) provide a command line interface to *all* ipol articles
2) provide a unified IPOL interface to many languages (numpy, octave, lua, ...)

The idea is that each IPOL article is described by a single text file, written
in IDL (Ipol Description Language).  This file specifies the URL of the source
code of the article; the compilation instructions; the names, types and default
values of the input and output parameters; and the way to call the compiled
code of the article.

The IDL files of all the algorithms are stored on the directory
"~/.config/ipol/idl/".   This can be created and filled-in manually and its the
files can be edited by hand using a text editor.  It can also be filled-in
automatically by running "clipol.py download_idls".

The downloaded and compiled sources, and the binaries, of an algorithm X are
stored on the directory "~/.cache/ipol/X" according to the following hierarchy:
	~/.cache/ipol/X/dl/src.tar.gz (original source code of the article)
	~/.cache/ipol/X/src/ (decompressed source code tree)
	~/.cache/ipol/X/bin/ (binary files associated to the article)
	~/.cache/ipol/X/tmp/ (temporary files created on each execution)

Each time that we want to run an algorithm "X", the file ~/.config/ipol/idl/X
is parsed and the tree under "~/.cache/ipol/X" is created if it didn't exist
already.  The original source code is downloaded and compiled locally.  Then
the algorithm is run to create the requested files.

Thus, for example, if we run

$ clipol.py ace lena.png out1.png
$ clipol.py ace lena.png out2.png

The files out1.png and out2.png will be identical (a color-corrected version of
the lena image) but the first run will be much slower because the whole source
code of the ACE algorithm will be downloaded and compiled.  The second run will
be very fast.  Thus, to try the ACE algorithm with several values of alpha we
can do

for i in {1..8}; do clipol.py ace lena.png lena_ace_$i.png -a $i ; done


