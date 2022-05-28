#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x_rev = ''
        for i in range(1, len(x) + 1):
            x_rev += x[-i]
        if x == x_rev:
            return True
        else:
            return False
        
# @lc code=end

