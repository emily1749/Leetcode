class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(substr):
            right = len(substr)-1
            for left in range(int(len(substr)/2)):
                if substr[left] is not substr[right]:
                    return False
                right -= 1
            return True
                
        res = []
        
        def backtrack(start, combo):
            if start >= len(s):
                res.append(combo[:])
                return
            for i in range(start, len(s)):
                substr = s[start:i+1]
                if is_palindrome(substr):
                    combo.append(substr)
                    backtrack(i+1, combo)
                    combo.pop()
        backtrack(0, [])
        return res
            