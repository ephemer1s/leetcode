#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = dict()
        for i in nums:
            if i in a:
                a[i] = False
            else:
                a[i] = True
        for i in a.keys():
            if a[i] == True:
                return i
# @lc code=end

