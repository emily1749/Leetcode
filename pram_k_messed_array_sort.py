'''
K-Messed Array Sort
Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[input] integer k

0 ≤ k ≤ 20
[output] array.integer



[1, 4, 5, 2, 3, 7, 8, 6, 10, 9]


[(1, 4, 5), (1, 4, 5, 2), (1, 4, 5, 2, 3), (4, 5, 2, 3, 7), ]

[1 , 2, ]

min heap 
'''


'''
import heapq

def sort_k_messed_array(arr, k):
  heap = arr[:k+1]
  heapq.heapify(heap)
  result = []
  
  for i in range(k+1, len(arr)):
    result.append(heapq.heappop(heap))
    heapq.heappush(heap, arr[i])
    
  return result

'''

'''
Time: O(n* log(k)) < nlogn
Space: O(k)
'''
import heapq

def sort_k_messed_array(arr, k):
  
  startIdx = 0
  endIdx = startIdx + k # 2
  minHeap = []
  
  i = 0
  while i < k:
    heapq.heappush(minheap, arr[i])
    i += 1
    
    '''
      1
    4   5
    
    '''
    
  while startIdx < len(arr): # 0 -> 9
    if endIdx < len(arr): # 2 < 9
      heapq.heappush(minheap, arr[endIdx])
      
    arr[startIdx] = heapq.heappop(minheap)
    startIdx += 1
    endIdx += 1
    
  return arr
    
