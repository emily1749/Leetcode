class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        indexes = {}
        for i in range(len(S)):
            indexes[S[i]] = i
        
        max_idx, start, partitions = 0, 0, []
        for i in range(len(S) + 1):
            if i <= max_idx: max_idx = max(max_idx, indexes[S[i]])
                
            else:
                partitions.append(max_idx - start + 1)
                if i<len(S): max_idx, start = indexes[S[i]], i
        return partitions
    
    #Space: O(N)
    #time: O(N) (two pass)