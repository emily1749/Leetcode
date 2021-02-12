class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = 0
        j = 0
        max_freq = 0
        hash = {}
        
        while j<len(s):
            if s[j] not in hash:
                hash[s[j]] = 0
            hash[s[j]]+=1
            max_freq = max(max_freq, hash[s[j]])
            if j-i+1>max_freq+k:
                hash[s[j-(max_freq+k)]]-=1
                i+=1
            j+=1
            
        return len(s)-i