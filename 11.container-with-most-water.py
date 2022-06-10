#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lptr, rptr, width, vol = 0, len(height) - 1, len(height) - 1, 0
        while lptr < rptr:
            if height[lptr] < height[rptr]:
                vol = max(vol, width * height[lptr])
                lptr = lptr + 1
            else:
                vol = max(vol, width * height[rptr])
                rptr = rptr - 1
            width = rptr - lptr
        return vol


        
# @lc code=end

