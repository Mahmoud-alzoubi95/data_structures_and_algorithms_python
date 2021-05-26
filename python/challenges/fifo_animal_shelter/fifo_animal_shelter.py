class Cat:
    def __init__(self,name,type="Cat"):
        self.name=name
        self.type=type
        self.next=None


class Dog:
    def __init__(self,name,type="Dog"):
        self.name=name
        self.type=type
        self.next=None

class Queue:
    

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, name,type):
        if type=="Cat":
            node = Cat(name)
        elif type=="Dog":
            node= Dog(name)
        else:
            return "type the correct name and type"

        if not self.front and not self.rear:
            self.front = node
            self.rear = node

        old_rear = self.rear
        self.rear = node
        old_rear.next = self.rear
  
    def dequeue_animal(self,type):
        """
        dequeue(extract) Node that fristly entered
        """

        if self.front:
            temp=self.front
            while temp:
                if temp.type==type:
                    self.front=temp.next
                    temp.next=None
                    if self.rear.name==temp.name:
                        self.front=None
                    return temp.name
                  
                else:
                    temp=temp.next
                    if self.front==self.rear:
                        break
        else:
            return "The queue is Empty"
        

    def __str__(self):
        output=''
        current=self.front
        while current:
            print(current.name)
            output+=f"{current.name} -> "
            current=current.next
            if self.front==self.rear:
                break
        output+= f"{None}"
        return output


if __name__=='__main__':
    q_animal=Queue()
    q_animal.enqueue("cat1","cat")
    q_animal.enqueue("cat2","Cat")
    q_animal.enqueue("Dog1","Dog")
    q_animal.enqueue("cat34","Cat")
    q_animal.enqueue("Dog2","Dog")
    print(q_animal)
    print('**********************')
    print(q_animal.dequeue_animal("Dog"))

