from python.challenges.Merge_Sort.Merge_Sort import *
import pytest

def test_insertion_sort():
    actual = mergeSort([6,2,7,0])
    excpected = [0,2,6,7]
    assert excpected == actual

def test_insertion_sort2():
    actual = mergeSort([30,20,15,8,3])
    excpected = [3,8,15,20,30]
    assert excpected == actual

def test_insertion_sort3():
    actual = mergeSort([5,12,7,8])
    excpected = [5, 7, 8, 12]
    assert excpected == actual

def test_insertion_sort4():
    actual = mergeSort([2,3,5,7,13,11])
    excpected = [2,3,5,7,11,13]
    assert excpected == actual