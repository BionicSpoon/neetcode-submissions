class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # only need to find out if it is possible to complete all courses from 0->numCourses-1
        # not compute and return a possible topo sort
        # do we need to topo sort w/ Khan's? Or can we just traverse and see if all
        # courses are hit. I think we can just traverse.

        # TRICKY - we must identify any loops and return False if so
        # So: We return False if: 1. Any course num < numCourses has no prereq to it
        #                            - This should catch all cases where a middle prereq is not hit
        #                         2. Any course has a prereq that leads to itself - not so easy

        # Because of #2, a simple traversal may not work
        # #1 is trivial to find -> do any course nums not appear in prereqs with a prereq
        # WRONG - you can take a course if it has no prereqs (duh)
        # Therefore, we only have to worry about loops
        # Khan's spots loops because it will never select nodes to be removed that
        # have no incoming edges - so if there are nodes left after it is done, there is a loop.
        # can we do the same thing we do in linked list loop detection problems? No, 
        # there could be a disconnected loop.

        # So, how to implement Khan's algo here?
        # 1. Scan prereqs for all prereq courses that have no prereqs, add to the queue
        # 2. Remove them one at a time -> remove all entries in prereqs with that course as a prereq (right side)
        # 3. For each course with a prereq removed, if it has no prereqs, add it to queue
        # 4. Repeat 2,3 until queue empty
        # 5. Return len(prereqs) == 0

        # I am confident in this approach - but is it efficient enough?
        # Based on hints, ig you could also do DFS from each starting prereq

        in_degrees = [0] * numCourses
        for after, prereq in prerequisites:
            in_degrees[after] += 1
        print(in_degrees)

        queue = deque() # contains only courses with no prerequisites
        for course_num, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                queue.append(course_num)
        
        print(f"{queue=}")
        while queue:
            prereq = queue.popleft()
            i = 0
            while i < len(prerequisites):
                if prerequisites[i][1] == prereq:
                    after = prerequisites.pop(i)[0]
                    in_degrees[after] -= 1
                    if in_degrees[after] == 0:
                        queue.append(after)
                else:
                    i += 1
        
        print(prerequisites)
        return len(prerequisites) == 0












