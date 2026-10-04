class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        size = [1] * len(edges + 1)

        def find(node):
            if parent[node] == node:
                return node
            
            parent[node] = find(parent[node])
            
            return parent[node]
        
        def union(n1, n2):
            root1 = find(n1)
            root2 = find(n2)

            if root1 == root2:
                return False

            if size[root1] < size[root2]:
                parent[root1] = root2
                size[root2] += size[root1]
            else:
                parent[root2] = root1
                size[root1] += size[root2]
            
            return True
        
        for u, v in edges:
            if not union(u, v):
                return[u,v]
    