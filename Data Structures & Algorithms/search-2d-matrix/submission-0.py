class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, n * m - 1

        while l <= r:
            m = l + ((r - l) // 2)
            row = m // n
            col = m % n

            if matrix[row][col] > target:
                l = m + 1
            elif matrix[row][col] < target:
                r = m - 1
            else:
                return True
            
        return False

            