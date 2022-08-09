#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            if targetSum == root.val and not root.left and not root.right:
                return True
            else:
                l = self.hasPathSum(root.left, targetSum - root.val)
                r = self.hasPathSum(root.right, targetSum - root.val)
                return l or r
        else:
            return False
# @lc code=end

