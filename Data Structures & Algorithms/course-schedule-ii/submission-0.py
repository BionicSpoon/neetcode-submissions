class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # exact same as Course Schedule, we just need to return a valid ordering
        # so, we just need to track each courseNum as we go.
        # also, start with all courses with no prereqs in the sequence list
        sequence = []
        in_degrees = [0] * numCourses
        neighbors = [[] for _ in range(numCourses)] # holds all courses this course is a prereq to

        for course, prereq in prerequisites:
            in_degrees[course] += 1
            neighbors[prereq].append(course)

        queue = deque()
        for course_num in range(numCourses):
            if in_degrees[course_num] == 0:
                queue.append(course_num)
                # sequence.append(course_num) no, do this later (when we pop from queue)

        while queue:
            prereq = queue.popleft()
            sequence.append(prereq)
            for neighbor in neighbors[prereq]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return sequence if len(sequence) == numCourses else []

        