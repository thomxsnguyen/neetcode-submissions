class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            if (r, c) in visited:
                return 0
            
            visited.add((r,c))

            area = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c - 1), dfs(r, c + 1)

            return area

        
        max_area = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, dfs(r, c))
        
        return max_area

