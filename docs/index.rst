WalkDir
=======

.. module:: walkdir
   :synopsis: Tools for iterating over filesystem directories

.. moduleauthor:: Nick Coghlan <ncoghlan@gmail.com>

.. toctree::
   :maxdepth: 2

The standard libary's :func:`os.walk` iterator provides a convenient way to
process the contents of a filesystem directory. This module provides higher
level tools based on the same interface that support filtering, depth
limiting and handling of symlink loops. The module also offers tools that
flatten the :func:`os.walk` API into a simple iteration over filesystem paths.

In this module, ``walk_iter`` refers to any iterator that yields
``path, subdirs, files`` triples of the style produced by :func:`os.walk`.

Path Iteration
--------------

Three iterators are provided for iteration over filesystem paths:

.. autofunction:: iter_paths

.. autofunction:: iter_dir_paths

.. autofunction:: iter_file_paths


Directory Walking
-----------------

A convenience API for walking directories with various options is provided:

.. autofunction:: filtered_walk

The individual operations that support the convenience API are exposed using
an :mod:`itertools` style iterator pipeline model:

.. autofunction:: include_dirs

.. autofunction:: include_files

.. autofunction:: exclude_dirs

.. autofunction:: exclude_files

.. autofunction:: limit_depth

.. autofunction:: handle_symlink_loops


Development and Support
----------------------

WalkDir is developed and maintained on BitBucket_. Problems and suggested
improvements can be posted to the `issue tracker`_.

.. _BitBucket: https://bitbucket.org/ncoghlan/walkdir/overview
.. _issue tracker: https://bitbucket.org/ncoghlan/walkdir/issues?status=new&status=open


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

