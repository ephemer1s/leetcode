#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversed = []
        if root is not None:
            if root.left is not None:
                traversed += self.postorderTraversal(root.left)
            if root.right is not None:
                traversed += self.postorderTraversal(root.right)
            traversed += [root.val]
        return traversed
# @lc code=end

'''
note:
Tree-Traversals:
https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
'''