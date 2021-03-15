# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head == None: return None
        length = 0
        curr = head
        while curr != None:
            curr = curr.next
            length += 1
                    
        if k%length== 0:
            return head
        
        slow = head
        fast = head
        prev_fast = ListNode()
        prev_fast.next = head
        prev_slow = ListNode()
        prev_slow.next = head
        # print(k)
        for i in range(k % length):
            fast = fast.next
            prev_fast = prev_fast.next
        
        while fast != None:
            prev_slow = prev_slow.next
            prev_fast = prev_fast.next
            fast = fast.next
            slow = slow.next
        
        prev_fast.next = head
        prev_slow.next = None
        return slow
            