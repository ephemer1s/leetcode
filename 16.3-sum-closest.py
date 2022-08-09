#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum
                elif sum > target:
                    if abs(sum - target) < abs(ret - target):
                        ret = sum
                    k = k - 1
                elif sum < target:
                    if abs(sum - target) < abs(ret - target):
                        ret = sum
                    j = j + 1
        return ret

'''
Two pointers
'''
# @lc code=end

