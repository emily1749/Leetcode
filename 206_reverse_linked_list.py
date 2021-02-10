# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        first = None
        nxt = head.next
        while nxt != None:
            head.next = first
            first = head
            head = nxt
            nxt = nxt.next
        head.next = first
        return head