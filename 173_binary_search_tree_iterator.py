# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        # self.pointer = self.startPointer()
        self.stack = []
        self.startPointer()
        
    def startPointer(self):
        curr = self.root
        stack = []
        while curr != None:
            stack.append(curr)
            curr = curr.left
        # self.pointer = curr
        # print(stack)
        self.stack = stack
        # print(self.stack)
        
    def next(self):
        """
        :rtype: int
        """
        # print(self.stack)
        # print(self.root)
        res = self.stack.pop()
        curr = res
        if curr.right: 
            curr = curr.right
            self.stack.append(curr)
            curr = curr.left  
            while curr:
                self.stack.append(curr)
                curr = curr.left
        return res.val

    def hasNext(self):
        """
        :rtype: bool
        """
        # print(self.stack)
        if len(self.stack)>0:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()