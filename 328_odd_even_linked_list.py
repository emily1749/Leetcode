# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        head_even = ListNode()
        head_odd = ListNode()
        even = head_even
        odd = head_odd
        counter = 1
        while head != None:
            if counter % 2 == 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            counter += 1
        odd.next = head_even.next
        even.next = None
        return head_odd.next