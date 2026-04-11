"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # we should store edges to make sure we never duplicate them
        # - they are the only unqiue elements. But can there be multiple nodes
        # with the same value?
        # NO - the index of each node in the adjacency list is the same as the node's value
        # remember: this adjacency list stores all neighbors of the node at each idx
        # - starting at node 1
        copy = {}
        
        def dfs(node):
            # print(f"dfs({node.val})")
            if not node:
                return None
            if node.val in copy:
                return copy[node.val]
            
            
            new_node = Node(node.val, [])
            copy[node.val] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            
            

            return new_node
        
        return dfs(node)

        
        # recursive: return a new node with the same neighbors (recursively called)
        if node.val in self.called_on:
            return
        
        
        # seen = set()
        # neighbors = []
        # queue = deque()
        # queue.append(node)
        # while queue:
        #     this_node = queue.popleft()
        #     if not this_node or this_node.val in seen:
        #         continue
        #     seen.add(this_node.val)
        #     cur_neighbors = []
        #     if not this_node:
        #         continue
        #     for neighbor in this_node.neighbors:
        #         queue.append(neighbor)
        #         cur_neighbors.append(neighbor.val)
        #     neighbors.append(cur_neighbors)

        # nodes = {n: Node(n) for n in range(1, len(neighbors) + 1)}
        # root = nodes[1] if nodes else None
        # for idx, cur_neighbors in enumerate(neighbors):
        #     idx += 1
        #     for neighbor_idx in cur_neighbors:
        #         nodes[idx].neighbors.append(nodes[neighbor_idx])
        # # prob do a hash map with ref to each Node(idx) map[idx:Node(idx)]
        # # then add to each map[idx].neighbors the respective edges in their neighbors and this neighbors
        # # return root
        # # profit
        # # this fucker.



        # return root