#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        neg = 2
        if x[0] == '-':
            neg = 1
            x = x[1:]
        ans = ''
        for i in range(1, len(x) + 1):
            ans += x[-i]
        ans = int(ans) * ((-1) ** neg)
        print(ans)
        # check overflow
        if -2147483648 < ans < 2147483647:
            return ans
        else: 
            return 0
# @lc code=end

