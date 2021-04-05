class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        result = []
        for num in range(len(arr), 0, -1):
            for i in range(len(arr)):
                if arr[i] == num:
                    arr = arr[:i+1][::-1] + arr[i+1:]
                    result.append(i+1)
                    arr = arr[:num][::-1] + arr[num:]
                    result.append(num)
                    break
        return result

                    
                    