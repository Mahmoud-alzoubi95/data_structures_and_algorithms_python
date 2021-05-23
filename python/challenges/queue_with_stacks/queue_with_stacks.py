from stacks_and_queues import Node,Stack

class Pseudo_Queue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.count = 0
        self.rear = 0
        

    def enqueue(self,value):
        """
        do enqueue with push methods from Stack
        """
        self.stack1.push(value)
        self.rear = self.stack1.top.value
        

    def dequeue(self):
        '''
        it used to return the first vlaue(node) in your 'PseudoQueue', first pushed:
        '''
        if self.stack2.is_empty():
            while self.count > 0:
                self.stack2.push(self.stack1.pop())
                self.count-=1
            result = self.stack2.pop()
            while True:
                self.stack1.push(self.stack2.pop())
                self.count +=1
                if self.stack2.is_empty():
                    return result
        else:
            return "stack is empty!"
                


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

   
