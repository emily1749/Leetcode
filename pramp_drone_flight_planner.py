def calc_drone_min_energy(route):
  leftover = 0
  refill = 0
  for i in range(1, len(route)):
    leftover += (route[i-1][2] - route[i][2])
    if leftover < 0:
      refill += abs(leftover)
      leftover = 0
  return refill


  '''
  [[0,2,10],[10,10,8]]
  '''
  
  
  
'''

10 -> 0 -> 6 -> 15 ->8
   +10  -6    -9   +7
leftover 4     0   +7  
provide        5

leftover 10, 4 -
refill = 0
for loop to run through z's from 1, len(route)
  leftover += (route[i-1] - route[i])
  if leftover < 0:
    refill += abs(leftover)
    leftover = 0
    
return refill
time:O(N) for N length of route
space: O(1)
 
'''
