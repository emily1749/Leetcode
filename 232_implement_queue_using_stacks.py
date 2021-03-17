class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.add_stack = []
        self.reversed_stack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.add_stack.append(x)
        #O(1)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        for i in range(len(self.add_stack)):
            self.reversed_stack.append(self.add_stack.pop())
        result = self.reversed_stack.pop()
        for i in range(len(self.reversed_stack)):
            self.add_stack.append(self.reversed_stack.pop())
        return result
        #O(N)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        # print(self.add_stack)
        for i in range(len(self.add_stack)):
            self.reversed_stack.append(self.add_stack.pop())
        # print(self.reversed_stack)
        result = self.reversed_stack[-1]
        for i in range(len(self.reversed_stack)):
            self.add_stack.append(self.reversed_stack.pop())
        return result
        #O(N)
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.add_stack)>0:
            return False
        else:
            return True
        #O(1)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()