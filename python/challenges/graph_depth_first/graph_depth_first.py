
from .graph import *

class NewGraph(Graph):

    def add_double_edge(self, start_Node, end_Node, weight_to=0, weight_from=None):
        weight_from = weight_to if weight_from == None else weight_from
        self.add_edge(start_Node,end_Node,weight_to)
        self.add_edge(start_Node,end_Node,weight_from)

    def depth_first(self, root):
        visited_lst = []
        visited_lst.append(root)

        def recurse_traverse(node):
            """Helper function to traverse using call stack"""
            neighbors = self.get_neighbors(node)
            print('neighbors', neighbors)
            for neighbor in neighbors:
                if neighbor[0] not in visited_lst:
                    visited_lst.append(neighbor[0])
                    print('passed-true. neighbor[0]', neighbor[0])
                    recurse_traverse(neighbor[0])
                
            return
        
        recurse_traverse(root)
        return visited_lst