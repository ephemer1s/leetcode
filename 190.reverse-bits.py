#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        s = '{:32b}'.format(n).replace(' ', '0')
        ans, pow = 0, 1
        for i in range(32):
            ans += int(s[i]) * pow
            pow *= 2
        return ans
# @lc code=end

