class DSU:
    def __init__(self, n):
        self.components = n
        self.parents = [x for x in range(n)]
        self.sizes = [1 for _ in range(n)]

    def find(self, n):
        while self.parents[n] != n:
            n = self.parents[n]
        return n
    
    def union(self, n1, n2):
        if self.find(n1) == self.find(n2):
            return False
        
        if self.sizes[self.find(n1)] < self.sizes[self.find(n2)]:
            n1, n2 = n2, n1
        
        self.parents[self.find(n2)] = self.find(n1)
        self.components -= 1
        self.sizes[self.find(n1)] += self.sizes[self.find(n2)]
        
        


# we just have to find the first duplicated union we attempt, since we only added one edge.
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for left, right in edges:
            left -= 1
            right -= 1
            print(left, right)
            if dsu.union(left, right) == False:
                return [left+1, right+1]
                
        return [-1, -1]