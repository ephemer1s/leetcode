#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        else:
            mat = ['' for i in range(numRows)]
            for i in enumerate(s):
                idx, ch = i[0], i[1]
                row = idx % (numRows * 2 - 2)
                if row >= numRows:
                    row = numRows * 2 - 2 - row
                mat[row] += ch
            ans = ''
            for i in mat:
                ans += i
        return ans

# @lc code=end
