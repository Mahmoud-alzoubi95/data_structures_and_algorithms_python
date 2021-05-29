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


if __name__=='__main__':

    bt = BinaryTree()
    bt.root = Node(7)
    bt.root.left = Node(13)
    bt.root.right = Node(5)
    bt.root.left.left = Node(8)
    bt.root.left.right = Node(9)
    bt.root.right.left = Node(1)
    bt.root.right.right = Node(-4)
    # bt.root.right.right.right = Node(100)
    print(bt)