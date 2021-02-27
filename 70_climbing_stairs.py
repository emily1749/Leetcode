class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #top down
        memory = {}
        
        def calc_steps(steps):
            if steps == 0 or steps == 1: return 1
            
            if steps in memory: return memory[steps]

            result = calc_steps(steps-1) + calc_steps(steps-2)
            memory[steps] = result
            
            return result
            
        return calc_steps(n) 
        
        #bottom up
#         cache = [False for _ in range(n+1)]
        
#         cache[0] = 1
#         cache[1] = 1
        
#         for i in range(2, n+1):
#             cache[i] = cache[i-1]+cache[i-2]
            
#         return cache[n]