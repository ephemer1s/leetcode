#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        amap = {}
        ans = []
        for i in range(len(nums)):
            amap[str(nums[i])] = i
        for i in range(len(nums)):
            if str(target - nums[i]) in amap:
                ans = [i, amap[str(target - nums[i])]]
                if ans[0] != ans[1]:
                    break
        ans = [min(ans), max(ans)]
        return ans 

# @lc code=end

