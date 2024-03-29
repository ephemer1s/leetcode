#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            if root.left and root.right:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
            elif root.left:
                return self.minDepth(root.left) + 1
            elif root.right:
                return self.minDepth(root.right) + 1
            else:
                return 1
        else:
            return 0
# @lc code=end

