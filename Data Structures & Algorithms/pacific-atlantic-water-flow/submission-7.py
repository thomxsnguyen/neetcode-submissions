class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # create sets for both pacific and atlnatic
        atlantic = set()
        pacific = set()

        ROWS = len(heights)
        COLS = len(heights[0])
        # traverse backwards from ocean

        def dfs(r, c, visited):
            visited.add((r,c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                
                # if a cell is out of bounds, we skip
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                
                # if we already visited this cell, we skip
                if (nr, nc) in visited:
                    continue

                # if the new cell is less than our current height. This is because we are traversing backwards
                if heights[nr][nc] < heights[r][c]:
                    continue
                
                dfs(nr, nc, visited)

        for c in range(COLS):
            dfs(0, c, pacific)
        
        for r in range(ROWS):
            dfs(r, 0, pacific)
        
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic)
        
        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic)
        
        return [(r,c) for r, c in pacific & atlantic]
        

                

