#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root:
            if targetSum == root.val and not root.left and not root.right:
                return [[root.val]]
            else:
                l = self.pathSum(root.left, targetSum - root.val)
                r = self.pathSum(root.right, targetSum - root.val)
                if l and r:
                    for i in l:
                        i.insert(0, root.val)
                    for i in r:
                        i.insert(0, root.val)
                    return l + r
                elif l:
                    for i in l:
                        i.insert(0, root.val)
                    return l
                elif r:
                    for i in r:
                        i.insert(0, root.val)
                    return r
        else:
            return None
# @lc code=end

