#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.dict = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if n not in self.dict:
            self.dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dict[n]
# @lc code=end

'''
TLE issues occured in followting code, why?
 - the time complexity is O(2^n) 
 - because there is no memory of results which caused massive repeated calculation.
 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
'''