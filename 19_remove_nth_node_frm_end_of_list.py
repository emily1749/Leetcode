# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None: return None
        # if head.next == None and n == 1: 
        #     return ListNode()
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        fast = dummy
        for i in range(n+1):
            # if fast.next:
            fast = fast.next
        while fast != None:
            fast = fast.next
            curr = curr.next
        print(curr)
        temp = curr.next.next
        curr.next = temp
        # print(head)
        return dummy.next
            