#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# Definition for a binary tree node.




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        return TreeNode(val = nums[len(nums) // 2],
                        left = self.sortedArrayToBST(nums[:len(nums) // 2]),
                        right = self.sortedArrayToBST(nums[len(nums) // 2 + 1:])
                        )
    
    
            
# @lc code=end

