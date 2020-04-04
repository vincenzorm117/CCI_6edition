
class Graph:
    def __init__(self, count=0):
        self.count = count
        self.edges = {}

    def connect(self, u,w):
        if u not in self.edges:
            self.edges[u] = set()
        self.edges[u].add(w)
    
    def find_all_distances(self, startNode):
        distances = [-1] * (self.count + 1)
        visitedNodes = set()
        q = [(startNode, 0)]
        while 0 < len(q):
            currNode, breadth = q.pop(0)
            if currNode not in self.edges:
                continue
            for node in self.edges[currNode]:
                if node not in visitedNodes:
                    visitedNodes.add(node)
                    q.append((node, breadth+1))
                    distances[node] = (breadth+1)*6
        for i in range(self.count+1):
            if i == startNode or i == 0:
                continue
            print(distances[i], end=" ")
        print()



t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x,y) 
    s = int(input())
    graph.find_all_distances(s)
    
