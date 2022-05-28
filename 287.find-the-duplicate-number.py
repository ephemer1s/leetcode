#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numdict = {}
        for i in nums:
            if i in numdict:
                return i
            else:
                numdict[i] = True
        
# @lc code=end

