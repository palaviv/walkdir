#!/usr/bin/env python3
"""test_iterwalk - unittests for the iterwalk module"""
import iterwalk
import unittest
import os.path

expected_files = "file1.txt file2.txt other.txt".split()

def fake_walk():
    subdirs = "subdir1 subdir2 other".split()
    files = expected_files
    root_dir = "root"
    yield root_dir, subdirs, files[:]
    for subdir in subdirs:
        dirname = os.path.join(root_dir, subdir)
        subdirs2 = subdirs[:]
        yield dirname, subdirs2, files[:]
        for subdir2 in subdirs2: 
            dirname2 = os.path.join(dirname, subdir2)
            yield dirname2, [], files[:]

expected_tree = [
    ('root', ['subdir1', 'subdir2', 'other'], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/subdir1', ['subdir1', 'subdir2', 'other'], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/subdir1/subdir1', [], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/subdir1/subdir2', [], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/subdir1/other', [], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/subdir2', ['subdir1', 'subdir2', 'other'], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/subdir2/subdir1', [], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/subdir2/subdir2', [], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/subdir2/other', [], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/other', ['subdir1', 'subdir2', 'other'], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/other/subdir1', [], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/other/subdir2', [], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/other/other', [], ['file1.txt', 'file2.txt', 'other.txt']),
]

depth_0_tree = [
    ('root', [], ['file1.txt', 'file2.txt', 'other.txt']),
]

depth_1_tree = [
    ('root', ['subdir1', 'subdir2', 'other'], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/subdir1', [], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/subdir2', [], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/other', [], ['file1.txt', 'file2.txt', 'other.txt']),
]

dir_filtered_tree = [
    ('root', ['subdir1'], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/subdir1', ['subdir1'], ['file1.txt', 'file2.txt', 'other.txt']),
    ('root/subdir1/subdir1', [], ['file1.txt', 'file2.txt', 'other.txt']),
]


class NoFilesystemTestCase(unittest.TestCase):
    
    # Sanity check on the test data generator
    def test_fake_walk(self):
        self.assertEqual(expected_tree, list(fake_walk()))

    def test_limit_depth(self):
        self.assertEqual(depth_0_tree, list(iterwalk.limit_depth(fake_walk(), 0)))
        self.assertEqual(depth_1_tree, list(iterwalk.limit_depth(fake_walk(), 1)))
        
    def test_filter_dirs(self):
        self.assertEqual(depth_0_tree, list(iterwalk.filter_dirs(fake_walk())))
        self.assertEqual(expected_tree, list(iterwalk.filter_dirs(fake_walk(), '*')))
        self.assertEqual(depth_0_tree, list(iterwalk.filter_dirs(fake_walk(), '*', exclude_filters=['*'])))
        self.assertEqual(dir_filtered_tree, list(iterwalk.filter_dirs(fake_walk(), 'sub*', exclude_filters=['*2'])))
        self.assertEqual(expected_tree, list(iterwalk.filter_dirs(fake_walk(), 'sub*', 'other')))

    def test_filter_files(self):
        for dirname, subdirs, files in iterwalk.filter_files(fake_walk()):
            self.assertEqual(files, [])
        for dirname, subdirs, files in iterwalk.filter_files(fake_walk(), '*'):
            self.assertEqual(files, expected_files)
        for dirname, subdirs, files in iterwalk.filter_files(fake_walk(), 'file*', 'other*'):
            self.assertEqual(files, expected_files)
        for dirname, subdirs, files in iterwalk.filter_files(fake_walk(), 'file*'):
            self.assertEqual(files, ['file1.txt', 'file2.txt'])
        for dirname, subdirs, files in iterwalk.filter_files(fake_walk(), 'file*', exclude_filters=['*2*']):
            self.assertEqual(files, ['file1.txt'])

# TODO: Create filesystem in temporary directory, add tests for the symlink loop detector

if __name__ == "__main__":
    unittest.main()
