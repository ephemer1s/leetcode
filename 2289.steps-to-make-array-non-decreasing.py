#
# @lc app=leetcode id=2288 lang=python3
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        stack = []
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                tmp = stack.pop()
                dp[i] = max(dp[i] + 1, dp[tmp])
                ans = max(ans, dp[i])
            stack.append(i)
        return ans

# @lc code=end
