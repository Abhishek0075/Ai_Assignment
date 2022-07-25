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
        
    def getAdj(self, index):
        adj=[]
        for i,v in enumerate(self.Mat[index,:]):
            if v!=0:
                adj.append(i)
        return adj
    
class DFS:
    def __init__(self,G,source):
        
        self.G = G
        self.source = source
        self.Q = []
        self.result = []

    def traverse(self):
        for i in range(self.G.N):
            self.G.setColor(i,WHITE)
            self.G.setParent(i,None)
        self.G.setColor(self.source,GREY)
        self.Q.append(self.source)
        while self.Q:
            u=self.Q.pop(0)
            