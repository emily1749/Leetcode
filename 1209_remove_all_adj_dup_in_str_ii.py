class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for char in s:
            if len(stack)>0 and char == stack[-1][0]:
                if stack[-1][1] == k-1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([char, 1])
        result = []
        for item in stack:
            char, count = item[0], item[1]
            for i in range(count):
                result.append(char)
        
        return "".join(result)
    
        #space: O(N)
        #time: O(N)