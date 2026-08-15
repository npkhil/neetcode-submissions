class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [0] * 9
        rows = [0] * 9
        boxes = [0] * 9
        for row in range(9):
            for col in range(9):
                cur = board[row][col]
                if cur == ".":
                    continue
                mask = 1 << (int(cur) - 1)
                box = row // 3 + (col // 3) * 3
                if mask & rows[row] or mask & cols[col] or mask & boxes[box]:
                    return False
                rows[row] |= mask
                cols[col] |= mask
                boxes[box] |= mask
        return True