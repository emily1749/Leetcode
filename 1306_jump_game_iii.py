class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        left = []
        right = []
        for idx in range(len(arr)):
            l = idx-arr[idx]
            r = idx+arr[idx]
            # if l>=0: 
            left.append(l)
            # else: left.append(-1)
            # if r<len(arr): 
            right.append(r)
            # else: right.append(-1)
        seen = set()
        def dfs(node):
            # if node < 0: return False
            # print(node)
            # print(left)
            # print(right)
            if arr[node] == 0:
                return True
            if node in seen:
                return False
            seen.add(node)
            if 0 <= left[node]  and dfs(left[node]):
                return True
            if right[node] < len(arr)  and dfs(right[node]):
                return True
            return False
        return dfs(start)