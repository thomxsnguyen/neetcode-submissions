class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        queue = deque()
        fresh = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = ((1,0), (-1,0), (0,1), (0,-1))

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr = nr + r
                    nc = nc + c

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    
                    if grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    fresh -= 1

                    queue.append((nr,nc))
            minutes += 1
        return minutes