#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
import numpy as np
class Solution:
    def isValid(self, arr):
        nums = {}
        for i in arr:
            if i not in nums:
                nums[i] = 1
            elif i != '.':
                return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = np.array(board)
        for i in range(9):
            if not self.isValid(board[i]):
                return False
        for i in range(9):
            if not self.isValid(board.T[i]):
                return False
        for i in [0,3,6]:
            for j in [0,3,6]:
                if not self.isValid(board[i:i + 3, j:j + 3].reshape(9)):
                    return False
        return True
# @lc code=end

