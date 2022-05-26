#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # One Liner:
        # return statistics.median(nums1+nums2)
                
        # Not the best answer: 
        merged_arr = []        
        while len(nums1) and len(nums2):
            if nums1[0] < nums2[0]:
                merged_arr.append(nums1.pop(0))
            else:
                merged_arr.append(nums2.pop(0))
        while len(nums1):
            merged_arr.append(nums1.pop(0))
        while len(nums2):
            merged_arr.append(nums2.pop(0))
        
        pos = (len(merged_arr) - 1) / 2
        if int(pos) == pos:
            return merged_arr[int(pos)]
        else:
            return (merged_arr[math.ceil(pos)] + merged_arr[math.floor(pos)]) / 2
# @lc code=end

