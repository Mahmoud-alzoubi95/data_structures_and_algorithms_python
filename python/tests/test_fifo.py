from python.challenges.fifo_animal_shelter.fifo_animal_shelter import *
import pytest 

def test_connection():
    pass

def test_one():
    q=Queue()
    q.enqueue("cat1","Cat")
    q.enqueue("cat2","Cat")
    q.enqueue("Dog1","Dog")
    q.enqueue("cat3","Cat")

    expected="cat1"
    actual=q.dequeue_animal("Cat")
    assert expected==actual

def test_two():
    q=Queue()
    q.enqueue("cat1","Cat")
    q.enqueue("cat2","Cat")
    q.enqueue("Dog1","Dog")
    q.enqueue("cat3","Cat")

    expected="Dog1"
    actual=q.dequeue_animal("Dog")
    assert expected==actual

def test_three():
    q=Queue()
    q.enqueue("cat1","Cat")
    q.enqueue("cat2","Cat")
    # q.enqueue("Dog1","Dog")
    q.enqueue("cat3","Cat")
    expected=None
    actual=q.dequeue_animal("Dog")
    assert expected==actual

def test_four():
    q=Queue()
    # q.enqueue("cat1","Cat")
    # q.enqueue("cat2","Cat")
    q.enqueue("Dog1","Dog")
    # q.enqueue("cat3","Cat")

    # q.enqueue("Simba","Cat")
    expected=None
    actual=q.dequeue_animal("Cat")
    assert expected==actual