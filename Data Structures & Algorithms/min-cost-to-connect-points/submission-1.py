class DSU:
    def __init__(self, n):
        self.parents = [x for x in range(n)]
        self.sizes = [1 for x in range(n)]

    def find(self, n):
        if self.parents[n] == n:
            return n
        self.parents[n] = self.find(self.parents[n])
        return self.parents[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            print("Already joined")
            return False
        if self.sizes[p2] > self.sizes[p1]:
            n1, n2 = n2, n1
            p1, p2 = p2, p1
        self.parents[p2] = p1
        self.sizes[p1] += self.sizes[p2]
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # Kruskal's gogogo
        # 1. Find all possible edges and sort them by distance
        edges = []
        ids = {}
        id_counter = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append((tuple(points[i]), tuple(points[j]), distance(points[i], points[j])))
            
            ids[tuple(points[i])] = id_counter
            id_counter += 1

        edges.sort(key=lambda x: x[2])

        edge_count = 0
        path_cost = 0
        dsu = DSU(len(points))
        edges = tuple(edges)
        for edge in edges:
            if not dsu.union(ids[edge[0]], ids[edge[1]]):
                continue
            edge_count += 1
            path_cost += edge[2]
            if edge_count == len(points) - 1:
                return path_cost

        return 0
