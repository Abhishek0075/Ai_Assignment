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

class UCS:
    def __init__(self,G,source):
        self.G = G
        self.source = source
        self.Q = []
        self.result = []
        self.distance=0
    
    def traverse(self,G,u):
        self.Q.append(u)
        while self.Q:
            u=self.Q.pop(0)
            for v in self.G.getAdj(u):
                