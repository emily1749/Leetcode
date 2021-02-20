# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None: return None
        left_node = self.serialize(root.left)
        right_node = self.serialize(root.right)
        return str(root.val) + "," + str(left_node) + "," + str(right_node)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        
        
        def deserialize_helper(queue):
            value = queue.popleft()
            if value == "None": 
                return None
            else:
                node = TreeNode(value)
                node.left = deserialize_helper(queue)
                node.right = deserialize_helper(queue)
                return node
        
        if data == None: 
            return None
        else: 
            data = data.split(",")
            queue = collections.deque(data)
            print(queue)
            return deserialize_helper(queue)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))