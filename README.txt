Overview
========

walkdir is a simple set of iterator tools intended to make it
easy to manipulate and filter the output of os.walk() in a way
that is also easily applicable to any source iterator that
produces data in the same format.

It offers tools such as:

- glob-style filtering for file and directory names
- depth limiting for directory recursion
- flattening of output into simple sequences of path names
- detection of symlink loops when following symlinks


Maintenance status
==================

I'm currently looking for someone interested in taking over
walkdir maintenance, as I've moved on from the project I
originally wrote it for, and it currently comes after
CPython, the Python Packaging Authority and the Python Software
Foundation in my priorities for open source contributions.

The symlink handling bug reported in Issue #21 really
should be fixed though, and that bug report also shows
that Issues #10 and #11 (regarding some missing tests)
demonstrate the adage "if it's not tested, it's broken".

The Shining Panda CI service has been shutdown, so the
project also needs a new CI setup.

If anyone is interested in taking over, fixing issue
#21 with an appropriate test (so likely having to fix
#10 and #11 as well) would be the place to start.