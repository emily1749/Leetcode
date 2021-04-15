def isToeplitz(arr):
  height = len(arr)
  width = len(arr[0])
  
  for i in range(1, height):
    for j in range(1, width):
      if not arr[i][j] == arr[i-1][j-1]: #2 == 2
        return False
  return True



arr= [[1,2,3,4],[5,1,2,3],[6,5,1,2]]
isToeplitz(arr)
'''
ill run the code
[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]

for i in range(1, height):
  for j in range(1, width):
    if not matrix[i][j] == matrix[i-1][j-1]:
      return False
return True

So basically having a double for loop run through
each item and checking if the one previous diagonally is equal
if it's not then return False

time: O(MXN) m length of height, n length of width
space: O(1) - just using pointers so constant space

    
    
    
    
    


[[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]
 
 
 total diagonals: height+width-1

just looking at the indexes and seeing a pattern to run through them

[[(0,0), (0,1), (0, 3)]]
for i in range(height+width-1):
  
  
 
 

'''