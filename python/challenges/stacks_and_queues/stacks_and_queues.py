

class EmptyStackException(Exception):
  pass



class Node: 
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:   
    def __init__(self, node=None):
        self.top = node
  
    def push(self, value):
        if not self.top:
            self.top = Node(value)
        else:
            node = Node(value)
            node.next = self.top
            self.top = node
  


    def pop(self):
        """removes the node from the top of the stack, and returns the node’s value"""
        temp=self.top
        try:
                self.top = self.top.next
                temp.next = None
                return temp.value
        except Exception:
            return "stack is empty!"
  
    def is_empty(self):
        """ Returns True if Empty and false otherwise"""
        if self.top:
            return False
        return True

    def peek(self):
        """ Returns the value at the top without modifying the stack, raises an exception otherwise """
        try:
            if not self.is_empty():
                return self.top.value
    
        except Exception:
            return "peek is empty!"
  
    # def __str__(self):
    #     current = self.top
    #     items = []
    #     while current:
    #         items.append(str(current.value))
    #         current = current.next
    #     return "\n".join(items)
    def __str__(self):
        """ Returns a string representaiton of the linked list
            1 -> 3 -> 4 -> Null
        """
        # step 0 - create a new empty string
        list_data = ""
        # step 1 iterate over each node
        current = self.top
        while current:
        # step 2 - insert each data to the string
            list_data += "{ %s } -> " %(current.value)
    # step 2b:  move to the next item
            current = current.next
        list_data += "NULL"
        # step 3 - return the final string
        return list_data

class Queue:   
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """ Add an item to the rear fo the queue """
        node = Node(value)

        if not self.front:
         # we have an emtpy queue
            self.front = node
            self.rear = node
        else:
        # make sure the previous rear will now point to the new node
            self.rear.next = node
      # move our rear to point to the new node
            self.rear = self.rear.next

    def is_empty(self):
        """ Returns True if Empty and false otherwise"""
        if self.front:
            return False
        return True

    def peek(self):
        """ Returns the value at the front without modifying the stack, raises an exception otherwise """
        try:
            if not self.is_empty():
                return self.front.value
    
        except AttributeError:
            return "queue is empty!"

    def dequeue(self):
        try:
            temp=self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        except AttributeError:
            return "queue is empty!"
    def __str__(self):
        """ Returns a string representaiton of the linked list
            1 -> 3 -> 4 -> Null
        """
        # step 0 - create a new empty string
        list_data = ""
        # step 1 iterate over each node
        current = self.front
        while current:
        # step 2 - insert each data to the string
            list_data += "{ %s } -> " %(current.value)
    # step 2b:  move to the next item
            current = current.next
        list_data += "NULL"
        # step 3 - return the final string
        return list_data
    # def __str__(self):
    #     current = self.front
    #     items = []
    #     while current:
    #         items.append(str(current.value))
    #         current = current.next
    #     return "\n".join(items)


if __name__ == "__main__":
  stack = Stack()
  # print(stack)
  # print(stack.peek())
  stack.push(0)
#   print(stack)
  stack.push(1)
  stack.push(25)
  # print(stack)
  # print(stack.peek())
  print(stack)

  queue = Queue()
#   print(queue)
  queue.enqueue("1")
#   print(queue)
  queue.enqueue("2")
  queue.enqueue("3")
#   print(queue.dequeue())
  print(queue)
#   print(stack.pop())
  