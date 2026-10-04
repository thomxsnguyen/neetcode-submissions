class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}

        for course, preq in prequisites:
            graph[preq].append(course)
        
        visited = set()
        path = set()
        order = []

        def dfs(course):
            if course in path:
                return False
            
            if course in visited:
                return True
            
            path.course(course)

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            path.remove(course)
            visitor.add(course)
            order.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
    