from python.challenges.tree.tree import *
import pytest


def test_empty_binary_tree():
    """
    assert that tree has been initialized with None value
    """
    bt = BinaryTree()
    assert bt.root == None

def test_pre_order_traverse(prepare_bt):
    """
    Get data from fixture.
    assert that tree the exact preperation data in pre order sortation
    """
    actual = prepare_bt.preOrder()
    expected = [7, 13, 8, 9, 5, 1, -4]
    assert actual == expected

def test_in_order_traverse(prepare_bt):
    """
    Get data from fixture.
    assert that tree the exact preperation data in in order sortation
    """
    actual = prepare_bt.inOrder()
    expected = [8, 13, 9, 7, 1, 5, -4]
    assert actual == expected

def test_post_order_traverse(prepare_bt):
    """
    Get data from fixture.
    assert that tree the exact preperation data in post order sortation
    """
    actual = prepare_bt.postOrder()
    expected = [8, 9, 13, 1, -4, 5, 7]
    assert actual == expected

def test_bst_add_on_root():
    """
    Add to root of binary tree
    """
    bst = BinarySearchTree()
    bst.add(10)
    expected = 10
    actual = bst.root.value
    assert actual == expected

def test_bst_add_5_values(prepare_bst):
    """
    Add root and leaves andd assert that it matching the fixture data
    """
    bst = prepare_bst
    assert bst.root.value == 23
    assert bst.root.right.value == 42
    assert bst.root.left.value == 8
    assert bst.root.left.left.value == 4
    assert bst.root.right.left.value == 27

def test_bst_add_5_values_2(prepare_bst_2):
    """
    Add root and leaves andd assert that it matching the fixture data
    """
    bst = prepare_bst_2
    assert bst.root.value == 10
    assert bst.root.right.value == 27
    assert bst.root.left.value == -1
    assert bst.root.left.right.value == 4
    assert bst.root.left.right.left.value == 0





def test_contain_1(prepare_bst_2):
    """
    get fata from fixture 2
    Check if data is exist or not
    """
    bst=prepare_bst_2
    expected=True
    actual=bst.contains(10)
    assert expected==actual

def test_contain_2(prepare_bst_2):
    """
    get fata from fixture 2
    Check if data is exist or not
    """
    bst=prepare_bst_2
    expected=False
    actual=bst.contains(5)
    assert expected==actual

def test_contain_3(prepare_bst_2):
    """
    get fata from fixture 2
    Check if data is exist or not
    """
    bst=prepare_bst_2
    expected=True
    actual=bst.contains(-1)
    assert expected==actual


    
@pytest.fixture
def prepare_bt():
    """ 
    fixture 1
    Preperation of data to to added to the tree
    bt -{tree of nodes}
    """
    bt = BinaryTree()
    bt.root = Node(7)
    bt.root.left = Node(13)
    bt.root.right = Node(5)
    bt.root.left.left = Node(8)
    bt.root.left.right = Node(9)
    bt.root.right.left = Node(1)
    bt.root.right.right = Node(-4)
    return bt

@pytest.fixture
def prepare_bst():
    """ 
    fixture 2
    Preperation of data to to added to Binary SEarch tree
    bst-{Binary tree}
    """
    bst = BinarySearchTree()
    bst.add(23)
    bst.add(8)
    bst.add(4)
    bst.add(42)
    bst.add(27)
    return bst

@pytest.fixture
def prepare_bst_2():
    """ 
    Preperation of data to to added to Binary SEarch tree
    bst-{Binary tree}
    """
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(-1)
    bst.add(4)
    bst.add(0)
    bst.add(27)
    return bst
