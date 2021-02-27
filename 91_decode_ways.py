class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        memory = {}
        def calc_ways(string, pointer):
            # print(pointer)
            if pointer>=len(string):
                return 1
            if s[pointer] == "0": return 0
            if pointer in memory: return memory[pointer]
            count_left, count_right = 0, 0
            if pointer+1<=len(string):
                count_left = calc_ways(string, pointer+1)
            if int(string[pointer:pointer + 2]) <= 26 and pointer+2<=len(string):
                count_right = calc_ways(string, pointer+2)
            
            result = count_left + count_right
            memory[pointer] = result
            return result
        
        return calc_ways(s, 0)
        