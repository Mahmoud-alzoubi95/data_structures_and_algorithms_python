class Node:
    def __init__(self,data):
        self.data=data

class Graph:

    def __init__(self,made_up_graph={}):
        self.adjacency_list=dict()
        self.edgs={}

    def add_node(self,data1,data2):
        node = Node(data1)
        neighbors_node=Node(data2)
        
        def node_add(node,neighbors_node):
           
            if node.data in self.adjacency_list.keys():
                print("appended")
                self.adjacency_list[node.data].append(neighbors_node.data)
            else :
                print("new_add")
                
                self.adjacency_list[node.data]=[neighbors_node.data]
            
        node_add(node,neighbors_node)
        node_add(neighbors_node,node)

        return f"A node with {data1} and another node with {data2} was added to the graph"
        
    
    def add_edge(self,f_node,sec_node,weight=1):

        
        keys=self.adjacency_list.keys()

            
        def add_edg(vertex,linked_node,weight):
            if vertex in self.edgs.keys():
                self.edgs[vertex].append((linked_node,weight))
                
            else:
                self.edgs[vertex]=[(linked_node,weight)]
        if f_node in keys and sec_node in keys :
            """
            To ensure the keys alraedy exist in graph
            """
            if f_node in self.adjacency_list[sec_node]:
                """
                To ensure the two nodes are connected together
                """
                add_edg(f_node,sec_node,weight)
                add_edg(sec_node,f_node,weight)
            return f"Edg was added successfully between {f_node} and {sec_node} with weight = {weight}"

        else:
            return "either nodes are not connected or one of them not exist in the graph"
        

    def GetNodes(self):
       
        return self.adjacency_list.keys()
        

    def GetNeighbors(self,node):
        return self.edgs[node]

        
    def getweight(self,s_node,l_node):
        if l_node in self.edgs.keys():
            print(self.edgs[s_node])
            for i in self.edgs[s_node]:
                if l_node == i[0]:
                
                    return i[1]
            

    def Size(self):
        return len(self.adjacency_list.keys())
   


if __name__ == "__main__":
    # g=Graph()
    # g.add_node("a","b")
    # g.add_node("a","c")
    # g.add_node("b","c")    
    # g.add_edge("a","c",100)
    # g.add_edge("a","b",800)
    # g.add_edge("c","b",100)
    # g.add_edge("v","b",500)
    g=Graph()
    g1=Graph()
    g.add_node("a","b")
    g.add_node("a","c")
    g.add_node("a","d")    
    g.add_node("b","c")
    g.add_node("b","d")  
    g.add_node("c","d") 
    g.add_node("d","f") 
    g1.add_node("1","2")
    g1.add_node("1","3")
    g1.add_node("1","4")
    g1.add_node("2","3")


    g.add_edge("a","b",800)
    g.add_edge("a","c",100)
    g.add_edge("a","d",50)
    g.add_edge("b","c",25)
    g.add_edge("b","d",10)
    g.add_edge("c","d",16)
    g.add_edge("d","f",17)
    # print(g.adjacency_list)
    # print(g1.adjacency_list)
    # print(g.add_edge("Mohammed","Ghafri",1))

    # print(g.adjacency_list.values())
    # print(g.Size())
    # # print(g.edgs)
    # print(g.GetNeighbors("a"))
    print(g.edgs)
    g.getweight("a","b")