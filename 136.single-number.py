#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from operator import xor


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bitsum = 0
        for i in nums:
            bitsum = xor(bitsum, i)
        return bitsum
# @lc code=end

