import math

class Djkastra:
    def __init__(self, graph = None):
        if graph == None:
            graph = {}
            
        self.graph = graph
    
    def insert(self, fr, to , value):
        self.graph[fr].append({to: value})
        
        
    def djkastra(self,start):
        length = {}
        for i in self.graph:
            length[i] = 9999999  
            
        length[start] = 0
        
        visited =[]
        visited.append(start)
        
        queue = []
        queue.append(start)
        
        while queue:
            top = queue.pop(0)
            for i in self.graph[top]:
                if i not in visited:
                    
        
              
        
        
        
        
        
 
path = {
    'a':{'b': 10},
    'b':{'c': 2},
    'c':{'a': 1}
}       

graph = Djkastra(path)
graph.djkastra('a')
    
        