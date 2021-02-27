class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #TOP DOWN
        
        memory = {}
        def calculate_coins(amount, count):
            if amount<0:
                return -1
            if amount == 0:
                return 0
            if amount in memory:
                return memory[amount]
            result = float('inf')
            for coin in coins:
                if amount-coin<0:
                    break
                current = calculate_coins(amount-coin, count) + 1
                result = min(current, result)
            memory[amount] = result
            return result
        
        coins.sort()
        result = calculate_coins(amount, 0)
        if result == float('inf'): return -1
        return result
        
        
        #BOTTOM UP
#         cache = [amount+1]*(amount+1)
#         cache[0] = 0
        
#         for i in range(1, amount+1):
#             minimum = cache[i]
#             for coin in coins:
#                 if i-coin>=0:
#                     minimum = min(minimum, 1+cache[i-coin])
#             cache[i] = minimum
        
#         if cache[amount] == amount+1: return -1
        
#         return cache[amount]
        