class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0 or len(tasks) == 0: return len(tasks)
        
        max_heap = []
        counts = collections.Counter(tasks)
        counts = [-freq for letter, freq in counts.items()]
        heapq.heapify(counts)
        
        total = len(tasks)
        most_freq = -(heapq.heappop(counts))
        required_inbetween = n*(most_freq - 1)
        while len(counts)>0:
            curr = -(heapq.heappop(counts))
            required_inbetween -= min(most_freq-1, curr)
        if required_inbetween>0:
            return len(tasks) + required_inbetween
        return len(tasks)
    
#         while len(counts)> 0 and n>0:
#             while len(counts) > 0 and required_inbetween > 0:
#                 required_inbetween -= -(heapq.heappop(counts))
            
#             n-=1
#         next_freq = -(heapq.heappop(counts))
#         if not next_freq == most_freq:
            
#         count_n = n
#         while next_freq == most_freq and n >0:
#             count_n -= 1
#             next_freq = -(heapq.heappop(counts))
        
        
        
        
        
#         total_tasks = len(tasks)
#         max_letter = ""
#         max_count = 0
#         counts = defaultdict(int)
#         for i in range(len(tasks)):
#             counts[tasks[i]] += 1
#             if counts[tasks[i]] > max_count:
#                 max_count = counts[tasks[i]]
#                 max_letter = tasks[i]
        