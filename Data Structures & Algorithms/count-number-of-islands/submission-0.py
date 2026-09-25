class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROW = len(grid)
        COLUMN = len(grid[0])
        islands = 0
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COLUMN:
                return

            if grid[r][c] == "0":
                return

            if (r,c) in visited:
                return

            visited.add((r,c))

            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c - 1) # Left
            dfs(r, c + 1) # Right
        
        for r in range(ROW):
            for c in range(COLUMN):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    dfs(r,c)
                    
        return islands