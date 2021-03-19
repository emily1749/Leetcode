class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = [asteroids[0]]
        # for i in range(1, len(asteroids)):
        i = 1
        while i<len(asteroids):
            if len(stack)> 0 and asteroids[i]<0 and stack[-1]>0:
                if abs(asteroids[i]) == stack[-1]:
                    stack.pop()
                    i+=1
                elif abs(asteroids[i]) > stack[-1]:
                    stack.pop()
                elif abs(asteroids[i]) < stack[-1]:
                    i+=1
            else:
                stack.append(asteroids[i])
                i+=1
        
        return stack
    
        # time: O(N)
        # space: O(N) for the stack to return