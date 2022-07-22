#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1]]
        for i in range(numRows - 1):
            l, r = ans[-1].copy(), ans[-1].copy()
            l.append(0)
            r.insert(0, 0)
            ans.append([x + y for x, y in zip(l, r)])
        return ans
                    
        
# @lc code=end

