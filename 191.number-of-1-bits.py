#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            if n % 2 == 1:
                ans += 1
            n = n // 2
        return ans
# @lc code=end

