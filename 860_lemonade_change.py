class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change = defaultdict(int)
        
        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                if change[5] < 1: return False
                change[5] -= 1
                change[10] += 1
            elif bill == 20:
                if change[10] >= 1 and change[5] >= 1:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False
        return True
        
        #time: O(N)
        #space: O(1)