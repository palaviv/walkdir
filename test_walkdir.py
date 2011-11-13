#!/usr/bin/env python3
"""test_walkdir - unittests for the walkdir module"""
import walkdir
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

all_paths = [
'root',
'root/file1.txt',
'root/file2.txt',
'root/other.txt',
'root/subdir1',
'root/subdir1/file1.txt',
'root/subdir1/file2.txt',
'root/subdir1/other.txt',
'root/subdir1/subdir1',
'root/subdir1/subdir1/file1.txt',
'root/subdir1/subdir1/file2.txt',
'root/subdir1/subdir1/other.txt',
'root/subdir1/subdir2',
'root/subdir1/subdir2/file1.txt',
'root/subdir1/subdir2/file2.txt',
'root/subdir1/subdir2/other.txt',
'root/subdir1/other',
'root/subdir1/other/file1.txt',
'root/subdir1/other/file2.txt',
'root/subdir1/other/other.txt',
'root/subdir2',
'root/subdir2/file1.txt',
'root/subdir2/file2.txt',
'root/subdir2/other.txt',
'root/subdir2/subdir1',
'root/subdir2/subdir1/file1.txt',
'root/subdir2/subdir1/file2.txt',
'root/subdir2/subdir1/other.txt',
'root/subdir2/subdir2',
'root/subdir2/subdir2/file1.txt',
'root/subdir2/subdir2/file2.txt',
'root/subdir2/subdir2/other.txt',
'root/subdir2/other',
'root/subdir2/other/file1.txt',
'root/subdir2/other/file2.txt',
'root/subdir2/other/other.txt',
'root/other',
'root/other/file1.txt',
'root/other/file2.txt',
'root/other/other.txt',
'root/other/subdir1',
'root/other/subdir1/file1.txt',
'root/other/subdir1/file2.txt',
'root/other/subdir1/other.txt',
'root/other/subdir2',
'root/other/subdir2/file1.txt',
'root/other/subdir2/file2.txt',
'root/other/subdir2/other.txt',
'root/other/other',
'root/other/other/file1.txt',
'root/other/other/file2.txt',
'root/other/other/other.txt'
]

all_dirs = [d for d in all_paths if not d.endswith('.txt')]
all_files = [f for f in all_paths if f.endswith('.txt')]


class NoFilesystemTestCase(unittest.TestCase):
    
    # Sanity check on the test data generator
    def test_fake_walk(self):
        self.assertEqual(expected_tree, list(fake_walk()))

    def test_limit_depth(self):
        self.assertEqual(depth_0_tree, list(walkdir.limit_depth(fake_walk(), 0)))
        self.assertEqual(depth_1_tree, list(walkdir.limit_depth(fake_walk(), 1)))
        
    def test_include_dirs(self):
        self.assertEqual(depth_0_tree, list(walkdir.include_dirs(fake_walk())))
        self.assertEqual(expected_tree, list(walkdir.include_dirs(fake_walk(), '*')))
        self.assertEqual(expected_tree, list(walkdir.include_dirs(fake_walk(), 'sub*', 'other')))

    def test_exclude_dirs(self):
        self.assertEqual(expected_tree, list(walkdir.exclude_dirs(fake_walk())))
        self.assertEqual(depth_0_tree, list(walkdir.exclude_dirs(fake_walk(), '*')))

    def test_filter_dirs(self):
        walk_iter = walkdir.include_dirs(fake_walk(), 'sub*')
        walk_iter = walkdir.exclude_dirs(walk_iter, '*2')
        self.assertEqual(dir_filtered_tree, list(walk_iter))

    def test_include_files(self):
        for dirname, subdirs, files in walkdir.include_files(fake_walk()):
            self.assertEqual(files, [])
        for dirname, subdirs, files in walkdir.include_files(fake_walk(), '*'):
            self.assertEqual(files, expected_files)
        for dirname, subdirs, files in walkdir.include_files(fake_walk(), 'file*', 'other*'):
            self.assertEqual(files, expected_files)
        for dirname, subdirs, files in walkdir.include_files(fake_walk(), 'file*'):
            self.assertEqual(files, ['file1.txt', 'file2.txt'])

    def test_exclude_files(self):
        for dirname, subdirs, files in walkdir.exclude_files(fake_walk()):
            self.assertEqual(files, expected_files)
        for dirname, subdirs, files in walkdir.exclude_files(fake_walk(), '*'):
            self.assertEqual(files, [])
        for dirname, subdirs, files in walkdir.exclude_files(fake_walk(), 'file*', 'other*'):
            self.assertEqual(files, [])
        for dirname, subdirs, files in walkdir.exclude_files(fake_walk(), 'file*'):
            self.assertEqual(files, ['other.txt'])

    def test_filter_files(self):
        walk_iter = walkdir.include_files(fake_walk(), 'file*')
        walk_iter = walkdir.exclude_files(walk_iter, '*2*')
        for dirname, subdirs, files in walk_iter:
            self.assertEqual(files, ['file1.txt'])

    def test_iter_paths(self):
        self.assertEqual(all_paths, list(walkdir.iter_paths(fake_walk())))

    def test_iter_dir_paths(self):
        self.assertEqual(all_dirs, list(walkdir.iter_dir_paths(fake_walk())))

    def test_iter_file_paths(self):
        self.assertEqual(all_files, list(walkdir.iter_file_paths(fake_walk())))

# TODO: Create filesystem in temporary directory, add tests for the symlink loop detector

if __name__ == "__main__":
    unittest.main()
