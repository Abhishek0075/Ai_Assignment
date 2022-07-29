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
    def __init__(self,G,source,maxD,goal):
        self.G=G
        self.source=source
        self.maxD=maxD
        self.goal=goal
    def traverse(self,u,path,level):
        path.append(self.source)
        if(self.source==self.goal):
            return (path)
        elif(level==self.maxD):
            return False
        for v in self.G.getAdj(self.source):
            if(self.traverse(v,path,level+1)==True):
                return (path)
            else:
                path.remove(v)
        return False

import numpy as np
M = np.array([[0,1,1,0,0],
              [1,0,0,1,0],
              [1,0,0,1,1],
              [0,1,1,0,1],
              [0,0,1,1,0]])
print(M)
G = Graph(M)
dls = DLS(G,1,3,3)
path=[]
dls.traverse(path,0)
dls.printResult()
