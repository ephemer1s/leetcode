#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = dividend / divisor
        if ans == 2147483648:
            return int(ans - 1)
        elif ans < 0:
            return math.ceil(ans)
        else:
            return math.floor(ans)
        
# @lc code=end

