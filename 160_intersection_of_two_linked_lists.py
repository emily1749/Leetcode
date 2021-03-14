# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        a_length = 0
        b = headB
        b_length = 0
        while a != None:
            a=a.next
            a_length += 1
        while b!= None:
            b = b.next
            b_length += 1
        if a==b:
            intersect = True
        else:
            return None
        a = headA
        b = headB
        if a_length>b_length:
            difference = a_length - b_length
            for i in range(difference):
                a = a.next
        elif a_length<b_length:
            difference = b_length - a_length
            for i in range(difference):
                b=b.next
        # print(a)
        # print(b)
        while a != None and b!= None:
            if a==b:
                return a
            else:
                a = a.next
                b = b.next