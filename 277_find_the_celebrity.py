# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.possible_celebrity = 0
        not_possible = {}
        for i in range(1, n):
            if knows(self.possible_celebrity, i) == 1:
                self.possible_celebrity = i
        for i in range(n):
            if i == self.possible_celebrity:
                continue
            if knows(i, self.possible_celebrity) == 0:
                return -1
            if knows(self.possible_celebrity, i) == 1:
                return -1
        return self.possible_celebrity
        
        # for a in range(n):
        #     for b in range(n):
        #         if a == b:
        #             continue
        #         if knows(a, b) == 1:
        #             array[b] += 1
        #             array[a] -= 1
        #         if array[a] == n-1:
        #             return 
        # for i in range(n):
        #     if array[i] == n-1:
        #         return i
        return -1