#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        DP with space optimization, O(m*n) in time, O(n) in space
        create 2 rows and fill in the 2nd row with numbers in prev row and prev element in this row
        '''
        prev = [0] * n
        for i in range(m):
            if i == 0:
                curr = [1] * n
            else:
                curr = [0] * n
                for j in range(n):
                    if j == 0:
                        curr[j] = 1
                    else:
                        curr[j] = prev[j] + curr[j - 1]
            prev = curr
        return curr[-1]
                
                
                                
        
# @lc code=end


'''
recover pascal triangle
#118 pascal triangle:
from scipy.special import comb
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [round(comb(rowIndex, i)) for i in range(rowIndex + 1)]

#so in this problem:
from scipy.special import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return round(comb(m + n - 2, min(m, n) - 1))

but why this is a dp problem?

'''
        