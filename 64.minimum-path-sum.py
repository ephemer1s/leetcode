#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
         DP with space opt, same as 62 unique paths '''
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if i == 0:
                curr = [sum(grid[0][:(i + 1)]) for i in range(n)]
            else:
                curr = [0] * n
                for j in range(n):
                    if j == 0:
                        curr[j] = prev[j] + grid[i][j]
                    else:
                        curr[j] = min(prev[j], curr[j - 1]) + grid[i][j]
            print(curr)
            prev = curr
        return curr[-1]
# @lc code=end

