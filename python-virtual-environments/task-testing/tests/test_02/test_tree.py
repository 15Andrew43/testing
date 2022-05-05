import pytest
import os

from tree_utils_02.tree import Tree


path_='/Users/andrew_borovets/Desktop/PROGA/MIPT/course3/PROM_PROGA/testing/1/python-virtual-environments/musor'


@pytest.fixture()
def tree_instance():
	print('------------------>   setUp')
	yield Tree()
	print('------------------>   tearDown')


def test_get(tree_instance):
	with pytest.raises(AttributeError):
		tree_instance.get('pepsdf', False)

	file_node = tree_instance.get(os.path.join(path_, 'pep'), False)
	assert 'pep' == file_node.name
	assert False == file_node.is_dir
	assert [] == file_node.children

	assert None == tree_instance.get(os.path.join(path_, 'pep'), True, True)

	with pytest.raises(AttributeError):
		tree_instance.get(os.path.join(path_, 'pep'), True)


	tree_instance.get(path_, False)




def test_filter_empty_nodes(tree_instance):
	assert None == tree_instance.filter_empty_nodes(
		tree_instance.
			get(
					os.path.join(path_, 'pep'),
					False
				),
		os.path.join(path_, 'pep')
	)

	tree_instance.filter_empty_nodes(
		tree_instance.
			get(
					os.path.join(path_, 'lol'),
					True
				),
		os.path.join(path_, 'lol')
	)

	tree_instance.filter_empty_nodes(
		tree_instance.
			get(
					path_,
					False
				),
		path_
	)
