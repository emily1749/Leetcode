class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counts = collections.Counter(S)
        counts = sorted([[freq, letter] for letter, freq in counts.items()])[::-1]
        result = [0 for _ in range(len(S))]
        most_freq = counts[0][0]
        if most_freq > len(S) - most_freq + 1: return ""
        result_idx, counts_idx = 0, 0
        while counts_idx < len(counts):
            while counts[counts_idx][0] > 0:
                if len(S)%2 == 0 and result_idx == len(S):
                    result_idx += 1
                result[result_idx%len(S)] = counts[counts_idx][1]
                counts[counts_idx][0] -= 1
                result_idx += 2
            counts_idx += 1
        return "".join(result)
            
        #space: O(N) for the array result, (counts array will be O(1))
        #time:sorting the counts: O(nlogn) ---running through it is o(n)
        
        
        # print(counts)
#         counts = sorted(counts)
#         print(counts)
        
        
        
        
#         max_freq = 0
#         max_letter = 0
#         letter_counts = {}
#         for letter in S:
#             letter_counts[letter] = letter_counts.get(letter, 0) + 1
#             if letter_counts[letter] > max_freq:
#                 max_freq = letter_counts[letter]
#                 max_letter = letter
            
#         other_freq = len(S) - max_freq
#         if max_freq - 1 <= other_freq:
#             result = ""
#             result += max_letter
#             letter_counts[max_letter] -= 1
#             for letter in letter_counts:
#                 if letter == max_letter:
#                     continue
#                 while letter_counts[max_letter]
#         else:
#             return ""