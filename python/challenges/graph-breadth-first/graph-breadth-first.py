from collections import deque

class Vertex:
    def __init__(self,data):
        self.data = data
    def __str__(self):
        return f"{self.data}"
class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)
class Graph:
    def __init__(self):
        self.adj_arr = {}
    def add_node(self, data):
        node = Vertex(data)
        self.adj_arr[node] = []
        return node
    def add_edge(self,node1=None,node2=None,weight1=0):
        if node1 not in self.adj_arr:
            raise KeyError
        elif node2 not in self.adj_arr:
            raise KeyError
        else:
            edge = Edge(vertex=node2,weight=weight1)
            self.adj_arr[node1].append(edge)
            edge = Edge(vertex=node1,weight=weight1)
            self.adj_arr[node2].append(edge)
    def get_nodes(self):
       return self.adj_arr.keys()
    def get_neighbors(self,node):
        return self.adj_arr.get(node,[])
    def size(self):
        return len(self.adj_arr)
    def breadth_first_search(self, start_vertex, action=(lambda x: None)):
        queue = Queue()
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            action(current_vertex)
            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor_vertex = edge.vertex

                if neighbor_vertex in visited:
                    continue
                else:
                    visited.add(neighbor_vertex)
                queue.enqueue(neighbor_vertex)