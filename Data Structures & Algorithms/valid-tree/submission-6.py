class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid tree conditions:
        # 1. All nodes must be connected
        # 2. There must be no cycles
        # 3. ??

        # Correct - all nodes must be connected with exactly one path
        # Can solve by doing a DFS from all starting points (or Kahn's algo?) and seeing
        # if they can reach all other points in exactly one way
        # And checking that there are no cycles during the DFS

        # Idk union find enough, but that would also work for ensuring all groups are connected

        # Can we run Kahn's algorithm from an arbitrary point and only on newly disconnected nodes?
        # Does it even work in an undirected graph? I think it's fine?
        # Can you just check if there are no duplicate edges - no this is given-
        # - and there are enough edges?
        # - and is each node involved in at least 1 edge

        # precompute hash map of all edges ?
        neighbors = {x: [] for x in range(n)}
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])

        # print(neighbors)

        is_cycle = False
        visited = set()
        def dfs(node: int, prev: int):
            nonlocal is_cycle
            if node in visited or is_cycle:
                is_cycle = True
                return False

            visited.add(node)
            # go to each neighbor except prev
            for nb in neighbors[node]:
                if nb != prev:
                    dfs(nb, node)

            return True
            # this should detech all cycles
            
            
        dfs(0, -1)


        return not is_cycle and len(visited) == n