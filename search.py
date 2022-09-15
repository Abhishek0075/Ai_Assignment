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


class DLS:
    def __init__(self,G,maxD,goal):
        self.G=G
        self.path=[]
        self.maxD=maxD
        self.level=1
        self.goal=goal
        
    def dls_traversal(self,S):
        self.path.append(S)
        self.G.setColor(S,BLACK)
        if S==self.goal:
            return self.path
        elif len(self.path)==self.maxD:
            return False
        else:
            self.level=self.level+1
        for v in self.G.getAdj(S):
            if self.G.getColor(v) == WHITE:
                temp=self.Traversal(v)
                if temp==True:
                    return self.path
                elif temp==self.path:
                    return self.path 
                else:
                    self.P.remove(v)
            return False 
    
    def dls_printResult(self):
        for u in self.path:
            print(u,end=' ')
        print('')
        
        
        
class BFS:
    
    def __init__(self,G,source):
        
        self.G = G
        self.source = source
        self.Q = []
        self.result = []
        
    def bfs_traverse(self):
        for i in range(self.G.N):
            self.G.setColor(i,WHITE)
            self.G.setParent(i,None)
            
        self.G.setColor(self.source,GREY)
        self.Q.append(self.source)
        while self.Q :
            u = self.Q.pop(0)
            for v in self.G.getAdj(u):
                if self.G.getColor(v) == WHITE:
                    self.G.setColor(v,GREY)
                    self.G.setParent(v,u)
                    self.Q.append(v)
            self.G.setColor(u,BLACK)
            self.result.append(u)
            
    def bfs_printResult(self):
        for u in self.result:
            print(u,end=' ')
        print('')
            

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


    def dsf_traverse(self):
        for i in range(self.G.N):
            self.G.setColor(i,WHITE)
            self.G.setParent(i,None)
        for i in range(self.G.N):
            if(self.G.getColor(i)==WHITE):
                self.G.setColor(i,GREY)
                self.visit(self.G,i)

    def dfs_printResult(self):
        for u in self.result:
            print(u,end=' ')
        print('')

import numpy as np

M=np.array([[0,1,1,0,0],
            [1,0,0,1,0],
            [1,0,0,1,1],
            [0,1,1,0,1],
            [0,0,1,1,0]])

G = Graph(M)
dfs = DFS(G)
dfs.dsf_traverse()
dfs.dfs_printResult()

G = Graph(M)
bfs = BFS(G,1)
bfs.bfs_traverse()
bfs.bfs_printResult()



G = Graph(M)
dls = DLS(G,3,3)
dls.dls_traversal(1)
dls.dls_printResult()
