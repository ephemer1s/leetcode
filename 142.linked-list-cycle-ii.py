#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = head, head
        while cur2 and cur2.next:
            cur2 = cur2.next.next
            cur1 = cur1.next
            if cur2 == cur1:
                break
        if not cur2 or not cur2.next:
            return
        else:
            cur1 = head
            while not cur2 == cur1:
                cur2 = cur2.next
                cur1 = cur1.next
            return cur1
        
# @lc code=end

