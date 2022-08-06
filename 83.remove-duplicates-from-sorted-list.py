#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            ptr = head
            while ptr.next is not None:
                while ptr.next.val == ptr.val:
                    ptr.next = ptr.next.next
                    if ptr.next == None:
                        break
                if ptr.next == None:
                        break
                ptr = ptr.next
        return head
# @lc code=end

