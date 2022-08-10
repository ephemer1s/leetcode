#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        DP with space opt, same as 62 unique paths
        '''
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        print(m, n)
        prev = [0] * n
        for i in range(m):
            curr = [1] * n
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                elif j == 0:
                    if i == 0:
                        curr[j] = 1
                    else:
                        curr[j] = prev[j]
                else:
                    curr[j] = curr[j - 1] + prev[j]
            prev = curr
            print(curr)
        return curr[-1]
# @lc code=end

