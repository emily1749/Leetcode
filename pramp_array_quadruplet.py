def find_array_quadruplet(arr, s):
  arr.sort()
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      remainder_needed = s - arr[i]- arr[j]
      sub_arr = list(arr[:i] + arr[i+1:j] + arr[j+1:])
      pointerA = 0
      pointerB = len(sub_arr) - 1
      while pointerA < pointerB:
        #print([i, j, pointerA, pointerB])
        #print(sub_arr)
        subtotal= sub_arr[pointerA] + sub_arr[pointerB]
        if subtotal == remainder_needed:
          return [arr[i], arr[j], sub_arr[pointerA], sub_arr[pointerB]]
        if subtotal < remainder_needed:
          pointerA += 1
        elif subtotal > remainder_needed:
          pointerB -= 1
  return []

print(find_array_quadruplet([2,7,4,0,9,5,1,3], 20))

'''

[2,7,4,0,9,5,1,3], 20

Expected:
[0,4,7,9]
Actual:
[0, 2, 4, 5]


[2, 7, 4, 0, 9, 5, 1, 3]    s = 20

 ^            ^     
 
 [0 , 1 , 3, 4, 5, 9]
        ^      ^
 pointerA
 pointerB
 for i in len(arr):
  for j in range(i, len(arr)):
    remainder_needed = s - arr[i]- arr[j]
    sub_arr = sorted(arr[i+1:j] + arr[j+1:])
    ponterA = 0
    pointerB = len(sub_arr) - 1
    for k in range(len(sub_arr)):
      subtotal= sub_arr[pointerA] + sub_arr[pointerB]
      subtotal == remainder_needed:
        return sorted([arr[i], arr[j], arr[pointerA], arr[pointerB]])
      if subtotal < remainder_needed:
        pointerA += 1
      elif subtotal > remainder_needed:
        pointerB -= 1
 time: O(n^3) N being length of arr
 space: O(n)
 
 2+7 = 9
 leftover = 11:
 know 9 < 11
 increment first pointer
 if we're over,
  increment the last pointer -= 1
three pointers
2+7+4 = 13
20-13 = 
2 + 7 + 0 = 9, searching 11


[7, 4, 0, 9]
[0, 4, 7, 9]
'''