Release History
---------------

0.4 (not yet released)
~~~~~~~~~~~~~~~~~~~~~~

* *SEMANTIC CHANGE*: to implement some of the fixes noted below, the
  ``all_paths`` iterator has been updated to emit paths in the following
  order for each directory produced by the underling iterator:

    * given directory if it appears to be a new root directory (i.e. it is
      not a subdirectory of the current root directory)
    * files in the given directory
    * subdirectories of the given directory

  Previously, directories were only emitted when walked by the underling
  iterator, which resulted in paths being missed in some cases.

* *SEMANTIC CHANGE*: to implement some of the fixes noted below, the
  ``dir_paths`` iterator has been updated to emit paths in the following
  order for each directory produced by the underling iterator:

    * given directory if it appears to be a new root directory (i.e. it is
      not a subdirectory of the current root directory)
    * subdirectories of the given directory

  Previously, directories were only emitted when walked by the underling
  iterator, which resulted in paths being missed in some cases.

* Thanks go to Aviv Palivoda for being the driving force behind this release,
  especially in addressing a variety of issues in the way directory filtering
  and symlinks to directories are handled.

* Issue #3: ``all_paths`` and ``dir_paths`` now correctly report symlinks to
  directories as directory paths, even when ``followlinks`` is disabled in
  the underlying iterator (fix contributed by Aviv Palivoda)

* Issue #4: ``all_paths`` and ``dir_paths`` now correctly report subdirectories
  at the maximum depth when the ``limit_depth`` filter is used to trim nested
  subdirectories (fix contributed by Aviv Palivoda)

* Issue #6: ``min_depth``, ``all_paths``, ``dir_paths``, and ``file_paths``
  all now work correctly with ``os.fwalk`` and other underlying iterators
  that produce a sequence with more than 3 elements for each directory
  (fix contributed by Aviv Palivoda)

* Issue #7: all filters now explicitly indicate in their documentation whether
  or not they support being used with bottom-up/depth-first traversal of the
  underlying directory hierarchy

* A temporary generated filesystem is now used to test symlink loop handling
  and other behaviours that require a real filesystem (patch contributed by
  Aviv Palivoda)

* development has migrated from GitHub to BitBucket

0.3 (2012-01-31)
~~~~~~~~~~~~~~~~~~

* (BitBucket) Issue #7: filter functions now pass the tuples created by underlying
  iterators through without modification, using indexing rather than
  tuple unpacking to access values of interest. This means WalkDir now
  supports any underlying iterable that produces items where ``x[0], x[1],
  x[2]`` refers to ``dirpath, subdirs, files``. For example, if the
  the iterable produces ``collections.namedtuple`` instances, those will be
  passed through to the output of a filtered walk.


0.2.1 (2012-01-17)
~~~~~~~~~~~~~~~~~~

* Add MANIFEST.in so PyPI package contains all relevant files


0.2 (2012-01-04)
~~~~~~~~~~~~~~~~

* (BitBucket) Issue #6: Added a ``min_depth`` option to ``filtered_walk`` and a new
  ``min_depth`` filter function to make it easier to produce a list of full
  subdirectory paths
* (BitBucket) Issue #5: Renamed path iteration convenience APIs:
   * ``iter_paths`` -> ``all_paths``
   * ``iter_dir_paths`` -> ``dir_paths``
   * ``iter_file_paths`` -> ``file_paths``
* Moved version number to a VERSION.txt file (read by both docs and setup.py)
* Added NEWS.rst (and incorporated into documentation)


0.1 (2011-11-13)
~~~~~~~~~~~~~~~~

* Initial release
