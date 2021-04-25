# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_less = less = ListNode()
        dummy_more = more = ListNode()
        cur = head
        while cur is not None:
            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                more.next = cur
                more = more.next
            cur = cur.next
        more.next = None
        less.next = dummy_more.next
        return dummy_less.next