class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, preq in prerequisites:
            graph[preq].append(course)
        
        path = set()

        def dfs(course):
            if course in path:
                return False
            
            path.add(course)

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            path.remove(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        

            
