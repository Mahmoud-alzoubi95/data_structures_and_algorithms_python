# from challenges.tree.tree import *
from tree import *


def breadth_first(self, tree):
        temp = []
        results = []
        
        if self.root:
            temp.append(self.root)
            
            while temp:
                node = temp.pop(0)
                results.append(node.value)
            
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            return results
        else:
            return 'Tree is empty'






def FizzBuzzTree(ary_tree):
    """
    Return a collection sorted by pre order
    output-{list}
    """
    output=[]
    def _walk(node):
        if not node:
            return
        # print(node.value)
        try :
            # print(node.value,node.value % 5 ==0 and node.value % 3==0)
            if node.value % 5 ==0 and node.value % 3==0:
                node.value='FizzBuzz'
            elif node.value % 5 ==0 :
                # print(node.value,node.value % 5 ==0)
                node.value='Buzz'
                # print(node.value)
            elif node.value % 3 ==0:
                node.value='Fizz'
            else :
                node.value=str(node.value)
        except:
            print(f"Error in this node which its value is  : {node.value}")

        output.append(node.value)
        _walk(node.left)
        _walk(node.right)

    _walk(ary_tree.root)
    return output




if __name__ == "__main__":
    bt=BinaryTree()
    bt.root=Node(2)
    bt.root.left=Node(4)
    bt.root.left.right=Node(30)
    bt.root.left.left=Node(12)
    bt.root.left.right=Node(18)
    bt.root.left.left=Node(10)
    # bt.root.left.left.right=Node("A")
    # bt.root.left.left.left=Node("B")
    bt.root.right=Node("m")
    bt.root.right.right=Node(18)
    bt.root.right.left=Node(10)
    
    print(FizzBuzzTree(bt))