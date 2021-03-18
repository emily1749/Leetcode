class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [False]*k
        self.first_idx = 0
        self.last_idx = 0
        self.k = k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        # if (self.last_idx + 1) % self.k == (self.first_idx % self.k):
        # print(self.queue)
        if self.isFull():
            return False
        self.queue[self.last_idx % self.k] = value
        self.last_idx += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        # if self.last_idx == self.first_idx:
        if self.isEmpty():
            return False
        self.queue[self.first_idx%self.k] = False
        self.first_idx += 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        # if self.last_idx == self.first_idx:
        # print(self.queue)
        if self.isEmpty():
            return -1
        return self.queue[(self.first_idx%self.k)]
        
    def Rear(self):
        """
        :rtype: int
        """
        # print(self.queue)
        # print(self.first_idx)
        # print(self.last_idx)
        if self.isEmpty():
            return -1
        return self.queue[(self.last_idx % self.k) - 1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        # print(self.queue)
        # print(self.first_idx)
        # print(self.last_idx)
        if self.last_idx == self.first_idx:
            return True
        return False

    def isFull(self):
        """
        :rtype: bool
        """
        # print(self.last_idx)
        if (self.last_idx - self.k) == (self.first_idx):
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()