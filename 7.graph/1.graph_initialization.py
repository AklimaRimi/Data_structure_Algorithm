class Graph:
    def __init__(self, graph = None):
        if graph == None:
            graph = {}
        
        self.graph = graph
    
    def insert(self, v, e):
        self.graph[v].append(e)
        
        


x = {
    'a' : ['b','c'],
    'b' : ['a','c'],
    'c' : ['b','a']
}

graph = Graph(x)

graph.insert("a","d")

graph.insert('b','d')
graph.insert('b','e')


print(graph.graph)
        
        

