from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
    def BFS(self, s): 
        visited = [False] * (len(self.graph))
        queue = [] 
        queue.append(s) 
        visited[s] = True
        while queue: 
            s = queue.pop(0) 
            print (s, end = " ") 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
    def DFSUtil(self, v, visited): 
        visited[v] = True
        print(v, end = ' ') 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
    def DFS(self, v): 
        visited = [False] * (len(self.graph)) 
        self.DFSUtil(v, visited) 

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 3)
g.addEdge(0, 6)
g.addEdge(1, 0) 
g.addEdge(1, 4) 
g.addEdge(1, 5) 
g.addEdge(2, 7) 
g.addEdge(2, 5) 
g.addEdge(3, 0) 
g.addEdge(3, 5)
g.addEdge(4, 1)
g.addEdge(4, 6)
g.addEdge(5, 1)
g.addEdge(5, 2)
g.addEdge(5, 3)
g.addEdge(6, 0)
g.addEdge(6, 4)
g.addEdge(7, 2)

g.BFS(0) 
print()
g.DFS(0)
