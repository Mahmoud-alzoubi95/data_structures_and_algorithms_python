from python.challenges.multi_bracket_validation.multi_bracket_validation import *
import pytest


def test_test():
    pass

def test_one_True():
    excepted = True
    actual = multi_bracket_validation("()")
    assert excepted == True

def test_Tow_False():
    excepted = False
    actual = multi_bracket_validation("{()")
    assert excepted == actual

def test_Three_False():
    excepted = False
    actual = multi_bracket_validation("()]")
    assert excepted == actual

def test_Three_False():
    excepted = False
    actual = multi_bracket_validation("(")
    assert excepted == actual