# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
         # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result    

    def end_of_first_half(self, head):
        fast = head.next.next
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
    
#         if head is None:
#             return None
#         first_half_end = self.end_of_first_half(head)
#         second_half_start = self.reverse_list(first_half_end.next)
#         result = True
        
#         first_position = head
#         second_position = second_half_start
#         while result and second_position is not None:
#             if first_position.val != second_position.val:
#                 result = False
#             first_position = first_position.next
#             second_position = second_position.next
#         first_half_end.next = self.reverse_list(second_half_start)
#         return result
#     def end_of_first_half(self, head):
#         slow = head
#         fast = head
#         while fast:
#             fast = fast.next.next
#             slow = slow.next
#         return slow
    
#     def reverse_list(self, head):
#         previous = None
#         current = head
#         while current is not None:
#             next_node = current.next
#             current.next = previous
#             previous = current
#             current = next_node
#         return previous
        #get length
#         array = []
#         while head != None:
#             array.append(head.val)
#             head = head.next
        
#         i=0
#         j = len(array)-1
#         while i<len(array)/2:
#             if array[i] != array[j]:
#                 return False