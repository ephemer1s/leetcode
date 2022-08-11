#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for i in nums:
            counts[i] += 1
        for i in range(len(nums)):
            if counts[0] > 0:
                nums[i] = 0
                counts[0] -= 1
            elif counts[1] > 0:
                nums[i] = 1
                counts[1] -= 1
            else:
                nums[i] = 2
        pass
                
# @lc code=end

'''
Original answer:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()
        
 - That's cheating! We need to find another way of doing this!
'''