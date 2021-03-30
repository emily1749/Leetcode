class Solution(object):
    def generateParenthesis(self, N):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def backtrack(left, right, combo):
            if right<left:
                return
            if right == 0 and left == 0:
                result.append("".join(combo))
                return
            if left>0:
                combo.append("(")
                backtrack(left-1, right, combo)
                combo.pop()
            if right>0:
                combo.append(")")
                backtrack(left, right-1, combo)
                combo.pop()
        backtrack(N, N, [])
        return result
                
        
        
        
        
        
#         result = []
#         def binary_search(current_combo, stackA, stackB):
#             if len(current_combo) == N + N:
#                 result.append(current_combo[:])
#                 return
#             if len(stackA) <= len(stackB) and len(stackA) > 0:
#                 stackA.pop()
#                 current_combo += "("
#                 binary_search(current_combo, stackA, stackB)
#                 stackA.append("(")
#                 current_combo = current_combo[:-1]
#             elif len(stackA) <= len(stackB) and len(stackB) > 0:
#                 stackB.pop()
#                 current_combo += ")"
#                 binary_search(current_combo, stackA, stackB)
#                 stackB.append(")")
#                 current_combo = current_combo[:-1]
        
#         binary_search("", ["(", "(", "("], [")", ")", ")"])
#         return result