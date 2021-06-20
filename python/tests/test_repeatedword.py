from python.challenges.repeated_word.repeated_word import *
import pytest

def test_repeat_a(text_sample):
    expected ='a'
    actual = lengthy_string(text_sample[0])
    assert expected==actual

def test_repeat_txtThree(text_sample):
    expected ='it'
    actual = lengthy_string(text_sample[1])
    assert expected==actual

def test_repeat_txtThree(text_sample):
    expected ='summer'
    actual = lengthy_string(text_sample[2])
    assert expected==actual


@pytest.fixture
def text_sample():

    a= "Once upon a time, there was a brave princess who..."
    it = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only"
    summer = "It was a queer, sultry summer , the summer they electrocuted the Rosenbergs , and I didn’t know what I was doing in New York.."

    return a, it, summer