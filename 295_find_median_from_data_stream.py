class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.max_heap) == 0:
            heapq.heappush(self.max_heap, num*-1)
        elif num < self.max_heap[0]*-1:
            heapq.heappush(self.max_heap, num*-1)
        else:
            heapq.heappush(self.min_heap, num)
        
        self.resize()
        return
        
    def resize(self):
        if len(self.max_heap) - len(self.min_heap) >= 2:
            heapq.heappush(self.min_heap, heapq.heappop(self.max_heap)*-1)
        elif len(self.min_heap) - len(self.max_heap) >= 2:
            heapq.heappush(self.max_heap, heapq.heappop(self.min_heap)*-1)
        return

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_heap) == len(self.max_heap):
            return(float(self.max_heap[0]*-1 + self.min_heap[0])/2)
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]*-1

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()