#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(set(nums))
        nums[:] = sorted(list(set(nums)))
        return k
# @lc code=end


'''
## Notes:
'list(set(nums))' does not work, 
and will gives array with negative like: '(0, 1, 3, -1)'

to modify external list variable 'nums', use
'nums[:]'
'''