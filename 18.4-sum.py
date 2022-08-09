#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) > 3:
            ret = set()
            nums.sort()
            for i in range(len(nums) - 3):
                for j in range(i + 1, len(nums) - 2):
                    k, l = j + 1, len(nums) - 1
                    while k < l:
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            ret.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))
                            k += 1
                            continue
                        elif nums[i] + nums[j] + nums[k] + nums[l] > target:
                            l -= 1
                        else:
                            k += 1
            return ret
        else:
            return []
# @lc code=end

'''
This is an owful O(n3)
How to optimize this?
'''