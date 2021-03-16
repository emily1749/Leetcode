# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        dummy = ListNode()
        dummy.next = head
        count = 0
        curr = dummy
        while count<m-1:
            curr = curr.next
            count += 1
        prev_left = curr
        curr = curr.next
        left = curr
        count += 1
        while count < n:
            curr = curr.next
            count += 1
        right = curr
        right_next = curr.next
        prev = right_next
        curr = left
        # nxt = curr.next
        while curr != None and curr != right_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            # nxt = nxt.next
        prev_left.next =  prev
        
        
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
#         counter = 1
#         return_head = head
#         nxt = head.next
#         first = head.next.next
#         while counter<m+1:
#             if counter<n:
#                 head = head.next
#                 nxt = nxt.next
#                 first = first.next

#             else:
#                 #start reversal
#                 nxt.next = head
#             counter++