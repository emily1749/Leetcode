class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # frequencies = defaultdict(int)
        # heap = []
        # for num in nums:
        #     frequencies[num] += 1
        # reversed_num = {}
        # for num in frequencies:
        #     number, freq = num, frequencies[num]
        #     reversed_num[freq] = number
        # for i in range(k):
        #     heapq.heappush(heap, frequencies[i])
        # print(Counter(nums).items())
        h = Counter(nums)
        # print(h)
        # print([h])
        d, h = [(freq, num) for num, freq in Counter(nums).items()], []
        # print(d)
        for i in range(k):
            heapq.heappush(h, d[i])
        # print(h)
        # print(d[0])
        # print(d[1])
        for i in range(k, len(d)):
            heapq.heappush(h, d[i])
            heapq.heappop(h)
        return [item[1] for item in h]