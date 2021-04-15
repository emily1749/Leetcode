def get_indices_of_item_wights(arr, limit):
  seen = {}
  for i in range(len(arr)):
    remaining_needed = limit - arr[i]
    if remaining_needed in seen:
      return [i, seen[remaining_needed]]
    seen[arr[i]] = i
  return []
  
'''
hash = {
  integer = index
  4, 0
  6, 1
  10, 2
}
arr = [4, 6, 10, 15, 16]
                  ^
       limit = 21
  21-4 = need 17
  21 - 6 = need 15
  21 - 10 = need 11
  
  [3, 1]
for loop run through arr
  if 
time: O(N)
space: O(N)




arr = sorted(arr)
  pointerA = 0
  pointerB = len(arr)-1
  while pointerA < pointerB:
    summation = arr[pointerA] + arr[pointerB]
    if summation == limit:
      return [pointerB, pointerA]
    elif summation > limit:
      pointerB -= 1
    else:
      pointerA += 1
  return []

print(get_indices_of_item_wights([4, 6, 10, 15, 16], 21))

  

[4,4,1]
[2, 1]

[1, 4, 4]
^      ^
[2, 0]

pointerA
pointerB

arr = [4, 6, 10, 15, 16]
       ^              ^      
take the sum of the two pointers
while pointerA < pointerB
  if arr[pointerA] + arr[pointerB] == lim:
    return [pointerB, pointerA]
  elif sum > lim:
    pointerB -= 1
  else:
    pointerA += 1
return []

  #if sum < lim:
time: O(N) N length of the array
space: O(1) 

for 
  for
O(N^2) 
    
[i, j]
lim = 21


[3, 1]


'''