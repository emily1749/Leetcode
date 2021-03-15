# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        nxt = prev.next
        curr = nxt.next
        last = curr.next
        while True:
            prev.next = curr
            curr.next = nxt
            nxt.next = last
            prev = prev.next.next
            if nxt.next == None:
                break
            nxt = nxt.next
            if curr.next.next.next == None:
                break
            curr = curr.next.next.next
            last = last.next.next
        
        return dummy.next
        
        
        
#         if head == None:
#             return None
      
        
#         curr = head.next
#         result_head = curr
#         prev = head
#         while curr.next and curr.next.next:
#             nxt = curr.next
#             curr.next = prev
#             prev.next = nxt.next
#             curr = prev.next
#             prev = nxt
        
#         curr.next = prev
#         prev.next = None
        
#         return result_head