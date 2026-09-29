class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       for row in board:
        for column in board:
            print(column) 