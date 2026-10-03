class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        queue = deque()

        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

            if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                continue
            
            if grid[nr][nc] != (2**31 - 1):
                continue
            
            grid[nr][nc] = grid[r][c] + 1
            queue.append((nr, nc))



