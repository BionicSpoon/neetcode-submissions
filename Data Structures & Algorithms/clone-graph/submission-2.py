"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.copy = {}
       # recursive dfs from each node, using self.copy to store copies of
       # previously visited nodes
        def dfs(node):
            if not node:
                return None
            if node.val in self.copy:
                return self.copy[node.val]
            new_node = Node(node.val)
            self.copy[new_node.val] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            

            return new_node

        return dfs(node)