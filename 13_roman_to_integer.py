class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        subtraction_cases = {
            "I": ["V", "X"],
            "X": ["L", "C"],
            "C": ["D", "M"]
        }
        i = 0
        res = 0
        while i < len(s):
            if s[i] in subtraction_cases and i+1 < len(s):
                if s[i+1] in subtraction_cases[s[i]]:
                    res += roman_numerals[s[i+1]] - roman_numerals[s[i]]
                    i += 2
                    continue
            res += roman_numerals[s[i]]
            i += 1
        return res