
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        nxt = head
        while nxt.next != None and nxt.next.next != None:
            nxt = nxt.next.next
            curr = curr.next
        
        if nxt.next == None:
            return curr
        
        else:
            return curr.next