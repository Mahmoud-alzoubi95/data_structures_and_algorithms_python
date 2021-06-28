    def breadth_first(self,graph):
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
            return 'graph is empty'