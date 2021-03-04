class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def wordBreakRecur(s, word_dict, start):
            if start == len(s):
                    return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and wordBreakRecur(s, word_dict, end):
                        return True
            return False

        return wordBreakRecur(s, set(wordDict), 0)
    
#         array = [False for _ in range(len(s)+1)]
#         array[0] = True
# #         
#         for i in range(1, len(s)+1):
#             for j in range(i):
#                 if array[j] == True:
#                     if s[j:i] in wordDict:
#                         array[i] = True
#                         break
                
#         return array[len(s)]
       