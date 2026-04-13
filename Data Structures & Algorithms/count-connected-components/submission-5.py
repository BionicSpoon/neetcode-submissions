class DSU:
    def __init__(self, n):
        self.components = n
        self.parents = [x for x in range(n)]
        self.size = [1] * n

    def find(self, n):
        # find with path compression - each recursive call will compress path to parent
        if self.parents[n] == n:
            return n
        self.parents[n] = self.find(self.parents[n])
        return self.parents[n]
        # while self.parents[n] != n:
        #     n = self.parents[n]
        # return n

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            print("Error? - loop found") # do not reduce self.components
            return
        # if self.size[p1] < self.size[p2]:
        #     n1, n2 = n2, n1

        self.parents[self.find(n2)] = self.find(n1)
        self.size[n1] += self.size[n2]
        self.components -= 1

    
    
    
    
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for edge in edges:
            dsu.union(edge[0], edge[1])

        return dsu.components
        