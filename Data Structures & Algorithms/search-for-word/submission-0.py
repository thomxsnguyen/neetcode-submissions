class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False

            if (r,c) in visited:
                return False
            
            if board[r][c] != word[i]:
                return False
            
            visited.add((r,c))
            found = (
                backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1)
            )
            visited.remove((r,c))

            return found
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False