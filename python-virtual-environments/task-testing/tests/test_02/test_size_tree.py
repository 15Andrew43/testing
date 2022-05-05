
import pytest
import os

from tree_utils_02.size_tree import SizeTree

path_='/Users/andrew_borovets/Desktop/PROGA/MIPT/course3/PROM_PROGA/testing/1/python-virtual-environments/musor'


@pytest.fixture()
def size_tree_instance():
	print('------------------>   setUp')
	yield SizeTree()
	print('------------------>   tearDown')


def test_construct_filenode(size_tree_instance):
	file_size_node = size_tree_instance.get(os.path.join(path_, 'lol'), False)
	assert 'lol' == file_size_node.name
	assert True == file_size_node.is_dir
	assert [] == file_size_node.children
	assert 4096 == file_size_node.size

	file_size_node = size_tree_instance.get(os.path.join(path_), False)
	assert 'musor' == file_size_node.name
	assert True == file_size_node.is_dir
	assert 8200 == file_size_node.size

	file_size_node = size_tree_instance.get(os.path.join(path_, 'pep'), False)
	assert 'pep' == file_size_node.name
	assert False == file_size_node.is_dir
	assert [] == file_size_node.children
	assert os.path.getsize(os.path.join(path_, 'pep')) == file_size_node.size