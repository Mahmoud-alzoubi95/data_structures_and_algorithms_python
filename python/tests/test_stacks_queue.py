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
Can successfully enqueue into a queue
Can successfully enqueue multiple values into a queue
Can successfully dequeue out of a queue the expected value
Can successfully peek into a queue, seeing the expected value
Can successfully empty a queue after multiple dequeues
Can successfully instantiate an empty queue
Calling dequeue or peek on empty queue raises exception

"""


def test_push(Stack_test):

    excpected = "{ 25 } -> { 1 } -> { 0 } -> NULL"
    actual = f"{Stack_test}"
    assert excpected == actual

def test_push_one(Stack_test_push):

    excpected = "{ 25 } -> NULL"
    actual = f"{Stack_test_push}"
    assert excpected == actual

def test_pop(Stack_test_pop):

    excpected = "stack is empty!"
    actual = f"{Stack_test_pop}"
    assert excpected == actual

def test_pop_one(Stack_test_pop_one):

    excpected = "25"
    actual = f"{Stack_test_pop_one}"
    assert excpected == actual


def test_peek(Stack_test_peek):

    excpected = "25"
    actual = f"{Stack_test_peek}"
    assert excpected == actual
# *****************************************






# *********************************


@pytest.fixture
def Stack_test():
    Stack_ = Stack()
    Stack_.push(0)
    Stack_.push(1)
    Stack_.push(25)
    return Stack_

@pytest.fixture
def Stack_test_peek():
    Stack_ = Stack()
    Stack_.push(0)
    Stack_.push(1)
    Stack_.push(25)
    a = Stack_.peek()
    return a

@pytest.fixture
def Stack_test_push():
    Stack_ = Stack()
    Stack_.push(25)
    return Stack_

@pytest.fixture
def Stack_test_pop(Stack_test):
    Stack_ = Stack()
    # Stack_.push(0)
    # Stack_.push(1)
    # Stack_.push(25)
    Stack_.pop()
    Stack_.pop()
    Stack_.pop()
    a = Stack_.pop()
    return a

@pytest.fixture
def Stack_test_pop_one(Stack_test):
    Stack_ = Stack()
    Stack_.push(0)
    Stack_.push(1)
    Stack_.push(25)
    a = Stack_.pop()
    return a



    