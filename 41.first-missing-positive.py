#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numdict = {}
        for i in nums:
            numdict[i] = True
        cnt = 1
        while 1:
            if cnt not in numdict:
                return cnt
            else:
                cnt += 1
        
# @lc code=end

