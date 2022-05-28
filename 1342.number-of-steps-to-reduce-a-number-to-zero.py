#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        return '{:b}'.format(num).count('1') + len('{:b}'.format(num)) - 1
# @lc code=end

