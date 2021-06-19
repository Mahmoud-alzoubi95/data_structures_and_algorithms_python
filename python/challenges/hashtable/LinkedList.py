class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add(self,data):
        node = Node(data)
        if self.head:
            node.next = self.head
        self.head = node
            


    def __str__(self) :
        list = ""
        current = self.head
        while current :
            list+=f"{current.data}--->"
            current=current.next
        list+="Null"

        return list



if __name__=='__main__':
    X = LinkedList()
    X.add('mahmoud')
    X.add('hasan')
    X.add('alzoubi')
    print(X)