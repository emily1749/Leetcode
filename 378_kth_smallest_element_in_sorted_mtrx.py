class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [(matrix[i][0], i, 0) for i in range(len(matrix)) if matrix[i]]
        heapq.heapify(heap)
        result = []
        
        for i in range(k):
            current = heapq.heappop(heap)
            curr_val = current[0]
            curr_row_idx = current[1]
            curr_col_idx = current[2]+1
            result.append(curr_val)
            if curr_col_idx < len(matrix[curr_row_idx]):
                # if len(matrix[curr_row_idx])<curr_col_idx:
                    heapq.heappush(heap, (matrix[curr_row_idx][curr_col_idx], curr_row_idx, curr_col_idx))
        print(result)
        return result[-1]