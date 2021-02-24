class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses == None: return []
        
        indegree = {numb: 0 for numb in range(numCourses)}
        adj_list = defaultdict(list)
        for courses in prerequisites:
            course, prereq = courses[0], courses[1]
            indegree[course] += 1
            adj_list[prereq].append(course)

        result = []
        queue = collections.deque([vertex for vertex in indegree if indegree[vertex] == 0])
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            indegree[vertex] -= 1
            for course in adj_list[vertex]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        if len(result) != numCourses: return []
        
        return result
            