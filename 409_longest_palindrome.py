class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_counts = {}
        for letter in s:
            char_counts[letter] = char_counts.get(letter, 0) + 1
        total_count = 0
        single_char = False
        for key in char_counts:
            if char_counts[key] %2 == 1:
                if single_char == False:
                    total_count += 1
                    single_char = True
                char_counts[key] -= 1
            total_count += char_counts[key]
        return total_count