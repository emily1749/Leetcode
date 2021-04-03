class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        counter = collections.Counter(words)
        counter = [(-freq, word) for word, freq in counter.items()]
        # print(counter)
        heapq.heapify(counter)
        result = []
        for i in range(k):
            result.append(heapq.heappop(counter)[1])
        
        return result
        # dictionary = defaultdict(list)
        # for i in range()
        
        # counter = list(collections.Counter(words).items())
        # print(counter)
        # words_dict = defaultdict(list)
        # for i in range(len(counter)):
        #     words_dict[counter[i][1]].append(counter[i][0])
        # print(words_dict)
        
        # counter_words = [(count, word) for word, count in counter.items()]
        # for word, count in counter:
            # print(word)
#         heap = counter_words[:k]
#         heapq.heapify(heap)
#         for i in range(k, len(counter_words)):
#             heapq.heappushpop(heap, counter_words[i])
#         result = []
#         i = 0
# #         while i <len(heap):
# #             if i == len(heap)-1:
            
# #             while 
            
#         return [word[1] for word in heap]