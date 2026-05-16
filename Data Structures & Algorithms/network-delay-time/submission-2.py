class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # seen set?
        # DSU needed? doubtful
        # can just query len(seen set)
        seen = {} # seen at
        time = {}
        neighbors = {}
        for start, end, t in times:
            time[(start, end)] = t
            if start in neighbors:
                neighbors[start].add(end)
            else:
                neighbors[start] = set((end,))

        # This could all be so much easier if we just use a stack and explore the shortest time first
        q = [(k, 0)] # [(node, absolute time)]
        while q:
            node, cur_time = q.pop(0)
            if node in seen:
                continue
            seen[node] = cur_time
            if node in neighbors:
                neighs: set = neighbors[node]
            else: # node has no neighbors it can go to
                continue
            for nb in neighs:
                q.append((nb, cur_time + time[(node, nb)]))
            

            q.sort(key=lambda x: x[1]) # ensure we always take the smallest next jump
                                       # should be very fast each time, right?

            



        

        # keep a queue of next nodes to visit
        # start with just the first node in it
        # when we visit a node:
        #   if node in seen -> do nothing? unless it was reached earlier in time
        #           -> then update the time it was reached?
        # makes sense -> make hash map seen[int: int]
        # if node in seen -> seen[node] = min(seen[node], time)
        # else: seen[node] = time
        # add all neighbors of popped from q node to q 
        # repeat until q is empty
        # return len(seen) = n
        # q = [k]
        # seen[k] = 0
        # while q:
        #     node: int = q.pop(0)
        #     if node in neighbors:
        #         neighs: set = neighbors[node]
        #     else: # node has no neighbors it can go to
        #         continue
        #     neighbors_to_remove = []
        #     for nb in neighs:
        #         time_from_here = seen[node] + time[(node, nb)]
        #         if nb in seen: # maybe don't need this? nah prob do, unless we sort? nah even then wouldn't work fs
        #             seen[nb] = min(seen[nb], time_from_here) # why do this an not append? doubtful good reason
        #             q.append(nb)
        #         else:
        #             seen[nb] = time_from_here
        #             if nb in neighbors and node in neighbors[nb]:
        #                 neighbors[nb].remove(node)
        #             neighbors_to_remove.append(neighbors[node])
        #             q.append(nb)
            
            
        print(seen)
        all_seen = len(seen) == n
        max_time = 0
        for n in seen:
            max_time = max(max_time, seen[n])
        return max_time if all_seen else -1