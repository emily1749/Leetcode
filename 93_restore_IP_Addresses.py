class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        
        def backtrack(combo, str_idx):
            if len(combo) == 4 and str_idx>= len(s):
                result.append(".".join(combo))
                return
            if len(combo) == 4: return
            for seg_length in range(1, 4):
                if str_idx+seg_length<=len(s):
                    segment = s[str_idx: str_idx+seg_length]
                else: continue
                if segment[0] == "0" and int(segment)>0: continue
                if int(segment)>255 or segment == "00" or segment == "000": continue
                combo.append(segment)
                backtrack(combo, str_idx+seg_length)
                combo.pop()
                
        backtrack([], 0)
        return result
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         result = []
        
#         def backtrack(index, combo, depth, prev):
#             if depth == 3:
#                 #check if valid combo, add valid combo
#                 #pop off the last "."
#                 if int(s[index:])>255:
#                     return
#                 #check if leading 0's
#                 if int(s[index:])>0 and int(s[idx: idx+i])<10 and len(s[idx: idx+i])>1:
#                     return
#                 result.append(combo)
#                 return
#             for i in range(3):
#                 if int(s[index: index+i])>255:
#                     continue
#                 #check if leading 0's
#                 if int(s[index: index+i])>0 and int(s[index: index+i])<10 and len(s[idx: idx+i])>1:
#                     continue
#                 length = len(combo)
#                 combo = combo + s[index:index+i] + "."
#                 backtrack(index + i, combo, depth+1, length)
#                 combo = combo[:length+1]
                
#         backtrack(0, [], 0, 0)
#         return result
                
        
        