# Define Node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# use a magic method so when you print node you see it's value
    def __str__(self):
        return f"{self.data}"

# Define linked list


class Linked_list:

  # Constructor
    def __init__(self):
        self.head = None

  # define your append method
    def append_node(self, data=None):
        new_node = Node(data)
    # Once we have a head
        if self.head:
            new_node.next = self.head  # set our current pointer to the head
        # Assign new_node to current.next
        self.head = new_node

# Define a method called includes which takes any value as an argument and returns a boolean result
# depending on whether that value exists as a Node’s value somewhere within the list.

    def includes(self,data):
        current=self.head
        while current:
            if data==current.data:
                print("True")
                return True
            else:
                current=current.next
        print("False")
        return False

    def __str__(self):
        """ Returns a string representaiton of the linked list
            1 -> 3 -> 4 -> Null
        """
        # step 0 - create a new empty string
        list_data = ""
        # step 1 iterate over each node
        current = self.head
        while current:
        # step 2 - insert each data to the string
            list_data += "{ %s } -> " %(current.data,)
        # step 2b:  move to the next item
            current = current.next
        list_data += "NULL"
        # step 3 - return the final string
        return list_data




# Print the Nodes
if __name__ == "__main__":
  linked = Linked_list()
#   linked.append_node()
  linked.append_node(27)
  linked.append_node("Alzoubi")
  linked.append_node("Mahmoud")
  print(linked)
#   print(linked.includes("khaled"),linked.includes("Mahmoud"),linked.includes(27))