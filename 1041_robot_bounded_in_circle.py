class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        if instructions == "": return True
        curr, direc_idx = [0, 0], 0
        direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(4):
            if (i == 1 or i == 2) and curr == [0, 0]: return True
            for instruction in instructions:
                if instruction == "G":
                    curr[0] += direc[direc_idx%4][0]
                    curr[1] += direc[direc_idx%4][1]
                elif instruction == "L":
                    direc_idx -=1
                    if direc_idx <0:
                        direc_idx += 4
                elif instruction == "R":
                    direc_idx += 1
        if curr == [0, 0]: return True
        return False
    
    #time: O(N) for N being the length of instructions
    #space: O(1)