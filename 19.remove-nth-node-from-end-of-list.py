#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. detect depth
        depth = 0
        cur = head
        while cur:
            depth += 1
            cur = cur.next
        # 2. find node
        m = depth - n
        if m == 0:
            return head.next
        cur = head
        while m > 1:
            cur = cur.next
            m -= 1        
        # 3. remove node
        cur.next = cur.next.next
        return head



# @lc code=end

