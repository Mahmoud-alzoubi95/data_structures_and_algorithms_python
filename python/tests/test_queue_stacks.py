from python.challenges.stacks_and_queues.stacks_and_queues import *
import pytest


"""
Can successfully push onto a stack x
Can successfully push multiple values onto a stack x
Can successfully pop off the stack x
Can successfully empty a stack after multiple pops x
Can successfully peek the next item on the stack x
Can successfully instantiate an empty stack x
Calling pop or peek on empty stack raises exception x
Can successfully enqueue into a queue x
Can successfully enqueue multiple values into a queue x
Can successfully dequeue out of a queue the expected value  x 
Can successfully peek into a queue, seeing the expected value x
Can successfully empty a queue after multiple dequeues x
Can successfully instantiate an empty queue 
Calling dequeue or peek on empty queue raises exception 

"""



def test_enqueue(queue_test_enqueue_multible):

    excpected = "{ 0 } -> { 1 } -> { 25 } -> NULL"
    actual = f"{queue_test_enqueue_multible}"
    assert excpected == actual

def test_test():
    pass

def test_dequeue(queue_test_enqueue):

    excpected = "{ 25 } -> NULL"
    actual = f"{queue_test_enqueue}"
    assert excpected == actual

def test_dequeue_multiple(queue_test_dequeue_multiple):

    excpected = "queue is empty!"
    actual = f"{queue_test_dequeue_multiple}"
    assert excpected == actual

def test_pop_one(queue_test_dequeue):

    excpected = "25"
    actual = f"{queue_test_dequeue}"
    assert excpected == actual

def test_peek(queue_test_peek):

    excpected = "0"
    actual = f"{queue_test_peek}"
    assert excpected == actual


@pytest.fixture
def queue_test_dequeue_multiple():
    queue = Queue()
    queue.enqueue(25)
    queue.enqueue(1)
    queue.enqueue(0)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    a = queue.dequeue()
    return a

@pytest.fixture
def queue_test_peek():
    queue = Queue()
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(25)
    a = queue.peek()
    return a

@pytest.fixture
def queue_test_enqueue():
    queue = Queue()
    queue.enqueue(25)
    return queue

@pytest.fixture
def queue_test_enqueue_multible():
    queue = Queue()
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(25)
    return queue

@pytest.fixture
def queue_test_dequeue():
    queue = Queue()
    queue.enqueue(25)
    queue.enqueue(1)
    queue.enqueue(0)
    a = queue.dequeue()
    return a