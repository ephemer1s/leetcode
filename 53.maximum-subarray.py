#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        if len(nums) == 1:
            return dp[0]
        else:
            for i, num in enumerate(nums[1:]):
                if dp[i] > 0:
                    dp.append(dp[i] + num)
                else:
                    dp.append(num)
        return max(dp)
# @lc code=end

