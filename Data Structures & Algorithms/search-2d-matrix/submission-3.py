class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if m == n == 1:
            return target == matrix[0][0]
        l = 0
        r = m*n - 1
        counter = 0
        while l <= r:
            c = (l + r) // 2
            row = c // n
            col = c % n
            val = matrix[row][col]
            print(l,r,c, val)
            if val < target:
                l = c + 1
            elif val > target:
                r = c - 1
            else:
                return True
        return False