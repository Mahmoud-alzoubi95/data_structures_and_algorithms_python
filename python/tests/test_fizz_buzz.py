# from python.challenges.tree.tree import *
from python.challenges.fizz_buzz_tree.fizz_buzz_tree import *


import pytest

def test_fizzbuzz_1(pre_data_1):
    """
     test for fizz and buzz, if the data is numbers
    """
    expected=['2', '4', 'Fizz', 'FizzBuzz', '7', 'Buzz', 'Fizz']
    actual  =FizzBuzzTree(pre_data_1)
    assert expected==actual


def test_fizzbuzz_2(pre_data_2):
    """
     test for fizz and buzz, if there is data that its non number
    """
    expected=['2', '4', 'Fizz', 'B', 'A', 'FizzBuzz', 'm', 'Buzz', 'Fizz']
    actual  =FizzBuzzTree(pre_data_2)
    assert expected==actual

def test_fizzbuzz_none(pre_data_2):
    """
     test for fizz and buzz, if there is no data at all
    """
    bt=BinaryTree()
    
    
    expected=[]
    actual  =FizzBuzzTree(bt)
    assert expected==actual


@pytest.fixture
def pre_data_1():
    bt=BinaryTree()
    bt.root=Node(2)
    bt.root.left=Node(4)
    bt.root.left.right=Node(30)
    bt.root.left.left=Node(12)
    bt.root.right=Node(7)
    bt.root.right.right=Node(18)
    bt.root.right.left=Node(10)
    return bt

@pytest.fixture
def pre_data_2():
    bt=BinaryTree()
    bt.root=Node(2)
    bt.root.left=Node(4)
    bt.root.left.right=Node(30)
    bt.root.left.left=Node(12)
    bt.root.left.left.right=Node("A")
    bt.root.left.left.left=Node("B")
    bt.root.right=Node("m")
    bt.root.right.right=Node(18)
    bt.root.right.left=Node(10)
    return bt
