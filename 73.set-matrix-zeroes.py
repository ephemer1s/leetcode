#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = set()
        rows = set()
        for rid, row in enumerate(matrix):
            for cid, col in enumerate(row):
                if col == 0:
                    rows.add(rid)
                    cols.add(cid)
        for row in rows:
            matrix[row][:] = [0] * len(matrix[0])
        for row in matrix:
            for col in cols:
                row[col] = 0
        pass
                
# @lc code=end

