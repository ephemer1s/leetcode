#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is not None and q is not None:
            if p.val != q.val:
                return False
            elif not self.isSameTree(p.left, q.right):
                return False
            elif not self.isSameTree(p.right, q.left):
                return False
            else:
                return True
        elif p is None and q is None:
            return True
        else: 
            return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root, root)

# @lc code=end

