from python.challenges.quick_sort.quick_sort import *
import pytest

def test_insertion_sort():
    actual = quickSort([6,2,7,0],0,3)
    excpected = [0,2,6,7]
    assert excpected == actual

def test_insertion_sort2():
    actual = quickSort([30,20,15,8,3],0,4)
    excpected = [3,8,15,20,30]
    assert excpected == actual

def test_insertion_sort3():
    actual = quickSort([5,12,7,8],0,3)
    excpected = [5, 7, 8, 12]
    assert excpected == actual

def test_insertion_sort4():
    actual = quickSort([2,3,5,7,13,11],0,5)
    excpected = [2,3,5,7,11,13]
    assert excpected == actual