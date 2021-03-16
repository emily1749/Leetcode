"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        stack = []
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        current = head
        # flatten_node(head, dummy)
        
        # def flatten_node(current, prev):
        while not(current == None and len(stack) == 0):
            if current == None and len(stack) > 0:
                current = stack.pop()
                current.prev = prev
                prev.next = current
                prev = current
                current = current.next
            while current!= None and current.child == None:
                prev = prev.next
                current = current.next
            if current != None and current.child != None:
                if current.next:
                    stack.append(current.next)
                temp = current.child
                current.child = None
                current.next = temp
                temp.prev = current
                prev = current
                current = temp
        return head
            