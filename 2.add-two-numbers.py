#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        carry = 0
        while l1 and l2:
            l1.val += l2.val + carry
            carry = int(l1.val / 10)
            l1.val %= 10
            if not l1.next and l2.next:
                l1.next = ListNode()
            elif not l2.next and l1.next:
                l2.next = ListNode()
            elif carry and not l1.next and not l2.next:
                l1.next = ListNode(val=1)
            l1 = l1.next
            l2 = l2.next
        
        return head
# @lc code=end

