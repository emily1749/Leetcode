"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # new_head = ListNode()
        # new_curr = new_head
        if head == None: return None
        curr = head
        nodes = {}
        # node[None] = None
        while curr != None:
            # new_curr.next = ListNode()
            # new_curr = new_curr.next
            # new_curr.val = curr.val
            new_node = ListNode(curr.val)
            nodes[curr] = new_node
            curr = curr.next
        curr = head
        while curr != None:
            new_curr = nodes[curr]
            if curr.next == None:
                new_curr.random = None
            else:  
                new_curr.next = nodes[curr.next]
            if curr.random == None:
                new_curr.random = None
            else:
                new_curr.random = nodes[curr.random]
            curr = curr.next
        new_curr.next = None
        return nodes[head]
        # new_curr = new_head
        # curr = head
        # while curr != None: