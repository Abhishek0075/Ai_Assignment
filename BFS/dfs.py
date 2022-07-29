WHITE = 0
GREY = 1
BLACK = 2

class Graph:
    
    def __init__(self,M):
        self.Mat = M
        self.N = M.shape[0]
        self.parent = [None for i in range(self.N)]
        self.color = [None for i in range(self.N)]
        
        
    def getParent(self,index):
        return self.parent[index]
        
    def getColor(self,index):
        return self.color[index]
    
    def setParent(self,index,P):
        self.parent[index] = P
        
    def setColor(self,index,color):
        self.color[index] = color
        
    def getAdj(self, node):
        adj=[]
        for i,v in enumerate(self.Mat[node,:]):
            if v!=0:
                adj.append(i)
        return adj
    
class DFS:
    def __init__(self,G):
        self.G = G
        self.result = []
    
    
    def visit(self,G,u):
        for v in self.G.getAdj(u):
            if(self.G.getColor(v)==WHITE):
                self.G.setColor(v,GREY)
                self.G.setParent(v,u)
                self.visit(G,v)
        self.G.setColor(u,BLACK)
        self.result.append(u)


    def traverse(self):
        for i in range(self.G.N):
            self.G.setColor(i,WHITE)
            self.G.setParent(i,None)
        for i in range(self.G.N):
            if(self.G.getColor(i)==WHITE):
                self.G.setColor(i,GREY)
                self.visit(self.G,i)

    def printResult(self):
        for u in self.result:
            print(u,end=' ')
        print('')

import numpy as np

M = np.array([[0,1,1,0,0],
              [1,0,0,1,0],
              [1,0,0,1,1],
              [0,1,1,0,1],
              [0,0,1,1,0]])
print(M)
G = Graph(M)
dfs = DFS(G)
dfs.traverse()
dfs.printResult()
