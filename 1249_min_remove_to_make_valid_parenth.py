class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        count = 0
        i = 0
        while i<len(s):
            if s[i] == ")" and len(stack) == 0:
                s = s[:i] + s[i+1:]
                continue
            elif s[i] == "(":
                stack.append("(")
            elif s[i] == ")" and len(stack)>0:
                count += 1
                stack.pop()
            i+=1
        if len(stack) == 0:
            return s
        i = 0
        while i< len(s):
            if count == 0 and s[i] == "(":
                s = s[:i] + s[i+1:]
                continue
            if count>0 and s[i] == "(":
                count -= 1
            i+=1
        return s
                
        #o(N)
        #o(N)