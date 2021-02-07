class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        hash_table = {}
        i=0
        maxCount = 0
        
        for j in range(0, len(s)):
            if s[j] in hash_table:
                i = max(hash_table[s[j]]+1, i)
            hash_table[s[j]] = j
            maxCount = max(maxCount, j-i+1)
            
            
        return maxCount
            
        # usedLetters = []
        # max_count = 0
        # count = 0
        # for letter in s:
        #     print(usedLetters)
        #     print(letter)
        #     print(count)
        #     if letter in usedLetters:
        #         #remove first element until not there
        #         while letter in usedLetters:
        #             usedLetters.pop(0)
        #             count-=1
        #     # else:
        #         # add to end of array
        #     usedLetters.append(letter)
        #     count+=1
        #     #max
        #     max_count=max(max_count, count)
        # return max_count