# checking whether a incomplete sudoku board is valid, without assuming the values for the empty boxes
# leetcode problem: https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/769/
# solution explanation: https://www.youtube.com/watch?v=TjFXEUCMqI8
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key (r/3, c/3)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
