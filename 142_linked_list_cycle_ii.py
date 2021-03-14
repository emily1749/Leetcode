# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while True:
            if slow == None or fast == None or fast.next == None or fast.next.next == None:
                return None
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        
        curr = head
        while curr != slow:
            curr = curr.next
            slow = slow.next
        
        return curr