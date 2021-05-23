import pytest
from python.challenges.queue_with_stacks.queue_with_stacks import *


def test_peek(queue_test_peek):

    excpected = "0"
    actual = f"{queue_test_peek}"
    assert excpected == actual


@pytest.fixture
def queue_test_enqueue():
    queue = Pseudo_Queue()
    queue.enqueue(25)
    queue.enqueue(1)
    queue.enqueue(0)
    print(queue)