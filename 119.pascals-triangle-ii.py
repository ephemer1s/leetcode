#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
from scipy.special import comb
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [round(comb(rowIndex, i)) for i in range(rowIndex + 1)]
# @lc code=end

'''
## Notes:
Pascal Triangle General Formula: $C^n_m$ for the 'm'th number in row 'n'

'''