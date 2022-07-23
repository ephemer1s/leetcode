#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        traversed = [root.val]
        if root.left is not None:
            traversed += self.preorderTraversal(root.left)
        if root.right is not None:
            traversed += self.preorderTraversal(root.right)
        return traversed
# @lc code=end

