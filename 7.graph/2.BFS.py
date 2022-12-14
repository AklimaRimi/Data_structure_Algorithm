class Graph:
    def __init__(self,graph = None):
        if graph == None:
            graph = {}
        self.graph = graph
    
    def insert(self,v,e):
        
        self.graph[v].append(e)
        
    def bfs(self,v):
        visited = [v]
        queue = [v]
        while queue:
            top = queue.pop(0)
            print(top)
            for V in self.graph[top]:
                if V not in visited:
                    visited.append(V)
                    queue.append(V)
                    
    def dfs(self,v):
        visited = [v]
        stack = [v]
        while stack:
            top = stack.pop()
            print(top)
            for V in self.graph[top]:
                if V not in visited:
                    visited.append(V)
                    stack.append(V)
        


paths = {
    'a':['b','d','i','e'],
    'b':['a','f','c','g'],
    'c':['b','h'],
    'd':['a','i','e'],
    'e':['a','i'],
    'f':['b','j','k'],
    'g':['b','h','m','l'],
    'h':['c','b','g','m'],
    'i':['d','e'],
    'j':['f'],
    'k':['f'],
    'l':['g'],
    'm':['g','h'],
        
}

graph  = Graph(paths)

print(graph.graph['b'])
print('DFS')
graph.dfs('g')
print('BFS')
graph.bfs('g')
