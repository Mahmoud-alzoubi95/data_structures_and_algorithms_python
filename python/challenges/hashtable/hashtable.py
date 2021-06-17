from .LinkedList import LinkedList
# from linkedlist_assets import LinkedList

class Hashtable:


    def __init__(self,size = 1024):
        self.map = [None] * size
        self.size = size

    def hash(self,key):
        hashed_total = 0
        for char in key:
            hashed_total += ord(char)
        return hashed_total * 7 % self.size

    def add(self,key,value):
        

        hashed_key = self.hash(key)

        if self.map[hashed_key] == None:

            self.map[hashed_key] = LinkedList(key)
            