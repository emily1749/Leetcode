class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        window = len(cardPoints) - k
        subtotal = sum(cardPoints[:window])
        minimum_window_sum = subtotal
        for i in range(window, len(cardPoints)):
            subtotal += (cardPoints[i] - cardPoints[i-window])
            minimum_window_sum = min(subtotal, minimum_window_sum)
        return sum(cardPoints) - minimum_window_sum
    
        #time: O(N)
        #space: O(1)