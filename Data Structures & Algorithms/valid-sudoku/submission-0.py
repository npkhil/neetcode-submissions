class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {0: set(), 1: set(), 2: set(),3: set(),4: set(),5: set(),6: set(),7: set(),8: set()}
        rows = {0: set(), 1: set(), 2: set(),3: set(),4: set(),5: set(),6: set(),7: set(),8: set()}
        boxes = {0: set(), 1: set(), 2: set(),3: set(),4: set(),5: set(),6: set(),7: set(),8: set()} # 0 1 2; 3 4 5; 6 7 8

        for row in range(len(board)):
            for col in range(len(board[row])):
                cur = board[row][col]
                box = col // 3 + (row // 3) * 3
                if cur == ".":
                    continue
                if cur in cols[col] or cur in rows[row] or cur in boxes[box]:
                    return False
                else:
                    cols[col].add(cur)
                    rows[row].add(cur)
                    boxes[box].add(cur)
        return True