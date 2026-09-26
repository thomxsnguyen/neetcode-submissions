class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        print(graph)

        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                if neighbor in visited:
                    return True
                
                if dfs(neighbor, node):
                    return True

            return False
        
        if dfs(0, -1):
            return False

        return len(visited) == n
                
            
