class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "": return []
        
        result = []
        
        letters = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': ['_']
        }
        
        def backtrack(index, combo):
            if index == len(digits):
                separator = ','
                result.append(separator.join(combo[:]).replace(",",""))
                return
            # print(digits[index])
            # print(letters[digits[index]])
            for letter in letters[digits[index]]:
                combo.append(letter)
                backtrack(index+1, combo)
                combo.pop()
        
        backtrack(0, [])
        return result
                