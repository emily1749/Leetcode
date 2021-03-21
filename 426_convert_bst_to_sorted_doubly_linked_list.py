"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None: return None
        self.dummy = Node()
        self.curr = self.dummy
        def traverse_inorder(node):
            if node.left: traverse_inorder(node.left)
            temp_right = node.right
            self.curr.right = node
            prev = self.curr
            self.curr = self.curr.right
            self.curr.left = prev 
            if temp_right: traverse_inorder(temp_right)
        traverse_inorder(root)
        temp = self.dummy.right
        self.curr.right = temp
        temp.left = self.curr
        # head = Node()
        # head.right = temp
        return self.dummy.right