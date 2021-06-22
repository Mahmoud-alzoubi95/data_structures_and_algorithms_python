class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
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

class Hashtable:

    def __init__(self,size = 1024):
        self.map = [None] * size
        self.size = size

    def hash(self,key):
        hashed_total = 0
        for char in key:
            hashed_total += ord(char)
        return hashed_total * 7 % self.size

    def add(self, key, value):
       hashed_key = self.hash(key)
       key_value = [key, value]
       if self.contains(key):
            current = self.map[hashed_key].head
            while current:
                if key == current.data[0]:
                    current.data[1] =  value
                current = current.next
                return self
       if self.map[hashed_key] is None:
           self.map[hashed_key] = LinkedList()
       self.map[hashed_key].append(key_value)
       return self.__str__()

    def get(self,key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            while self.map[hashed_key].head:
                if self.map[hashed_key].head.data[0] == key:
                    return self.map[hashed_key].head.data[1]
                self.map[hashed_key].head = self.map[hashed_key].head.next
            return "Not found"
        return "Not found"

    def contains(self,key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            current = self.map[hashed_key].head   
            while current:
                if current.data[0] == key:
                    return True
                current = current.next
            return False
        return False


    def __str__(self):
        output = ""
        for char in self.map:
            if char is not None:
                current = char.head
                while current:
                    output +=f"{current.data}-->" 
                    current = current.next
        output+='None'
        return output
    

"******************************************************************"
"code challenge 33"

def left_join(hash1,hash2):
    """[summary]

    Args:
        hash1 (bool): [description]
        hash2 (bool): [description]

    Returns:
        [type]: [description]
    """
    output = []
    single_elem = []
    for elem in hash1.map:
        if elem:
            current = elem.head          
            while current:
                single_elem.append(current.data[0])
                single_elem.append(current.data[1])
                if hash2.contains(current.data[0]):
                    single_elem.append(hash2.get(current.data[0]))
                else:
                    single_elem.append(None)
                output.append(single_elem)
                single_elem = []
                current = current.next
    return output


if __name__ == "__main__":
    h1 = Hashtable()
    h1.add('fond','enamored')        
    h1.add('fnod', 'anger')          
    h1.add('fodn', 'employed')    
    h1.add('donf', 'garb')           
    h1.add('ofnd', 'usher')

    h2 = Hashtable()
    h2.add('fond', 'averse')
    h2.add('fnod', 'delight')
    h2.add('fodn', 'idle')
    h2.add('guide', 'follow')
    h2.add('flow', 'jam')


    print(left_join(h1,h2))