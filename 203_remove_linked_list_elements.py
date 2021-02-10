
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        curr = ListNode()
        curr.next = head
        result_head = curr
        # curr = curr.next
        nxt = curr.next
        
        while nxt != None:
            if nxt.val != val:
                curr.next = nxt
                curr = nxt
            nxt = nxt.next
        curr.next = nxt
        
        return result_head.next
        
        
#         if head == None:
#             return head
#         result_list = ListNode()
#         result_head = result_list
#         curr = head
#         nxt = head.next
        
#         while not nxt == None:
#             if nxt.val != val:
#                 result_list.next = ListNode()
#                 result_list = result_list.next
#                 result_list.val = curr.val
#                 curr = nxt
#             nxt = nxt.next
            
       
#         if curr.val != val:
#             result_list.next = ListNode()
#             result_list = result_list.next
#             result_list.val = curr.val
#         result_list.next = None
#         return result_head.next
        