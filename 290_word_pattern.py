class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_array = list(pattern)
        str_array = s.split(" ")
        map_words = {}
        map_chars = {}
        if len(pattern_array) != len(str_array):
            return False
        for c, w in zip(pattern_array, str_array):
            if c not in map_chars:
                if w in map_words:
                    return False
                map_words[w] = c
                map_chars[c] = w
            else:
                if map_chars[c] != w:
                    return False
        return True
        
        # str_array = s.split(" ")
        # pattern_to_str = {}
        # # my_set = set()
        # str_to_pattern = {}
        # if len(pattern_array) != len(str_array):
        #     return False
        # for i in range(len(pattern_array)):
        #     if pattern_array[i] not in pattern_to_str and str_array[i] not in str_to_pattern:
        #         pattern_to_str[pattern_array[i]] = str_array[i]
        #         str_to_pattern[str_array[i]] = pattern_array[i]
        #     else:
        #         if pattern_to_str[pattern_array[i]] == str_array[i] and str_to_pattern[str_array[i]] == pattern_array[i]:
        #             continue
        #         # elif pattern_array[i] not in pattern_map and str_array[i] in my_set:
        #         else:
        #             return False
        # return True