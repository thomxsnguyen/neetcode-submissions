class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = 9
        rows = [set() for _ in range(n)]
        columns = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                value = board[i][j]
                box_index = (i // 3) * 3 + (j // 3)
                if value == '.':
                    continue
                if value in rows[i] or value in columns[j] or value in boxes[box_index]:
                    return False
                rows[i].add(value)
                columns[j].add(value)
                boxes[box_index].add(value)

        return True