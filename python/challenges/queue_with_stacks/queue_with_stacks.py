from stacks_and_queues import Node,Stack

class Pseudo_Queue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.rear = 0
        

    def enqueue(self,value):
        """
        do enqueue with push methods from Stack
        """
        self.stack1.push(value)
        self.rear = self.stack1.top.value
        

    def dequeue(self):
        """
        do dequeue with pop methods from Stack using FIFO
        """
        if self.stack1.is_empty() and self.stack2.is_empty():
            return 'empty queue !!!'
        elif self.stack2.is_empty():
            while self.stack1.top:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()


    def __str__(self):
        """
        return string of Queue
        output-{string}
        """
        output=''
        current=self.stack1.top
        while current:
            output+=f"{current.value} --> "
            current=current.next
        output+= "None"
        return output


if __name__ == "__main__":
    new = Pseudo_Queue()
    # new.enqueue("A")
    # new.enqueue("B")
    # new.enqueue("C")
    # print(new)
    # new.dequeue()
    new.dequeue()
    print(new)

   
