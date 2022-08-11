#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 1
        else:
            l = self.isBalanced(root.left)
            r = self.isBalanced(root.right)
            if not l or not r:
                return False
            else:
                if abs(l - r) > 1:
                    return False
                else:
                    return max(l, r) + 1
                
# @lc code=end

