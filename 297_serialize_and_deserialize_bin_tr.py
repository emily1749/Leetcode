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
        res = []
        def preorder(node):
            res.append(str(node.val))
            if node.left: 
                preorder(node.left)
            else: 
                res.append('.')
            if node.right: 
                preorder(node.right)
            else:
                res.append('.')
        preorder(root)
        #print(res)
        #print(','.join(res))
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == None: return None
        arr = data.split(',')
        #print(arr)

        def build(l):
            # if arr == None:
            #     return
            cur = l.pop(0)
            #print(cur)
            #print(l)
            if cur == ".":
                return None
            node = TreeNode(cur)
            node.left = build(l)
            node.right = build(l)
            return node
        res = build(arr)
        #print(res)
        return res
            
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))