class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i, total_profit = 1, 0
        
        while i < len(prices):
            while i<len(prices) and prices[i] < prices[i-1]: i+=1
            local_min = prices[i-1]
            while i< len(prices) and prices[i] > prices[i-1]:i+=1
            total_profit += (prices[i-1] - local_min)
            i += 1
                
        return total_profit
    
    
#         i = 1 
#         total_profit = 0
#         # local_min = prices[0]
#         # local_profit = 0
#         # prev = prices[0]
        
#         while i < len(prices):
#             while i<len(prices) and prices[i] < prices[i-1]:
#                 i+=1
#             local_min = prices[i-1]
                
#             while i< len(prices) and prices[i] > prices[i-1]:
#                 i+=1
#             # local_profit = local_min - prices[i-1]
#             # total_profit += local_profit
#             total_profit += (prices[i-1] - local_min)
            
#             # if prices[i] == prices[i-1]:
#             i += 1
                
#         return total_profit