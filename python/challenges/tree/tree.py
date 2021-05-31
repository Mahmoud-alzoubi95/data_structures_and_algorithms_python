class Node:
    """
    Declare Nodes with its values
    No return
    """
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None


class BinaryTree:
    def __init__(self):
        self.root=None


    
    def preOrder(self):
        """
        Return a collection sorted by pre order
        output-{list}
        """
        output=[]
        def _walk(node):
            if not node:
                return
            # print(node.value)
            output.append(node.value)
            _walk(node.left)
            _walk(node.right)

        _walk(self.root)
        return output

    def inOrder(self):
        """
        Return a collection sorted by in eorder
        output-{list}
        """
        output=[]
        def _walk(node):
            if not node:
                return
            _walk(node.left)
            output.append(node.value)
            _walk(node.right)
            

        _walk(self.root)
        return output

    def postOrder(self):
        """
        Return a collection sorted by post order
        output-{list}
        """
        output=[]
        def _walk(node):
            if not node:
                return
            _walk(node.left)
            _walk(node.right)
            output.append(node.value)
        _walk(self.root)
        return output


    def find_maximum_value(self):
        self.max=self.root.value
        # output=[]
        def _walk(node):
            if not node:
                return
            # print(node.value)
            # output.append(node.value)
            if node.value> self.max:
                self.max=node.value

            _walk(node.left)
            _walk(node.right)

        _walk(self.root)
        return self.max

    def breadth_first(self,visited, graph, node):
        self.visited = [] # List to keep track of visited nodes.
        self.queue = []     #Initialize a queue

        
        self.visited.append(node)
        self.queue.append(node)
        output=[]
        while self.queue:
            s = self.queue.pop(0) 
            # print (s, end = " ") 
            output.append(s)

            for neighbour in graph[s]:
                if neighbour not in visited:
                    self.visited.append(neighbour)
                    self.queue.append(neighbour)
        return output

class BinarySearchTree(BinaryTree):
    def add(self, value):

        """
        Add elements in form of binray search
        No return. Just sorting
        """
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            while (current):
                if current.value > value: # Got to left
                    if current.left == None: # if current is a leaf
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if current.right == None: # if current is a leaf
                        current.right = Node(value)
                        break
                    current = current.right

    def contains(self,value):
        """
        Test if the desired value is exist or not
        boolean return
        """

        current = self.root
        while (current):
                if current.value==value:
                    return True
                elif current.value > value: # Got to left
                    if current.left==value:
                        return True
                    current = current.left
                else:
                    if current.right==value:
                        return True
                    current = current.right
        return False




if __name__=='__main__':

    bt = BinaryTree()
    bt.root = Node(7)
    bt.root.left = Node(13)
    bt.root.right = Node(5)
    bt.root.left.left = Node(8)
    bt.root.left.right = Node(9)
    bt.root.right.left = Node(1)
    bt.root.right.right = Node(-4)
    bt.root.right.right.right = Node(100)

    bt_in=BinaryTree()
    print(bt.preOrder())
    print(bt.inOrder())
    print(bt.postOrder())
    bst=BinarySearchTree()
    bst.add(23)
    bst.add(8)
    bst.add(4)
    bst.add(42)
    bst.add(27)
    max_value=bt.find_maximum_value()
    print(max_value)
    # print(bt)
    # print(bst)
    graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
    }
    print(bt.breadth_first([],graph, 'A'))