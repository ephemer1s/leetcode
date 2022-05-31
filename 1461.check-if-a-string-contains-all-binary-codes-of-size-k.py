#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
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

