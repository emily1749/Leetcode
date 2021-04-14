def find_pairs_with_given_difference(arr, k):
  seen = set() #0, -1, -2, 2   at 1
  result = []
  for i in range(len(arr)):
    if arr[i] - k in seen:
      result.append([arr[i], arr[i]-k])
    seen.add(arr[i])
  seen = set()
  second_result = []
  for i in range(len(arr)-1, -1, -1):
    if arr[i] - k in seen:
      second_result.append([arr[i], arr[i]-k])
    seen.add(arr[i])
  return  result + second_result[::-1]
  # my_hash = {}
  # for i in range(len(arr)): #-1
  #   remaining = arr[i]-k # -1-1= -2*-1 = 2
  #   if remaining in my_hash:
  #     result.append([my_hash[remaining], remaining])
  #   my_hash[remaining] = arr[i] # {-1= 0, } y:x              
  # return result  
print(find_pairs_with_given_difference([0, -1, -2, 2, 1], 1))
print(find_pairs_with_given_difference([0, -1, -2, 2, 1], 1))


'''
    def find_pairs_with_given_difference(arr, k):
  seen = set() #0, -1, -2, 2   at 1
  result = []
  for i in range(len(arr)):
    if arr[i] - k in seen:
      result.append([arr[i], arr[i]-k])
  my_hash = {}
  for i in range(len(arr)): #-1
    remaining = arr[i]-k # -1-1= -2*-1 = 2
    if remaining in my_hash:
      result.append([my_hash[remaining], remaining])
    my_hash[remaining] = arr[i] # {-1= 0, } y:x              
    #z = arr[i] - k
    #if z in seen:
    #  result.append([arr[i], z])
    #seen.add(arr[i]) #{0}
  return result      
                 
                     #1-k = 1 - 0 = 1
                     # (1, 0)
                     #1 - 1 = 0 1-1 = 0
                    
                     
  
#arr = [0, -1, -2, 2, 1]
hash = {
y: x
-1: 0
}
seen = {0}
arr = [0, -1, -2, 2, 1], k = 1
       ^
0-1
need 1:
need = (arr[i]-k) * -1
put into the hashtable  need: curr_x

also put arr[i] into seen

-1 * -1 => 1
    

hash = {
 -1: 0
 2: -1
 -3: -2
 1: 2
}
seen = {0, -1, -2, 2}
arr = [0, -1, -2, 2, 1], k = 1

^ 



0 - ? = 1

0 - 1 = -1

0 - 1 = -1

0 - 1 ===> 1
[(0, -1), (-1, 2), (2, 1), (1, 0 )] 

O(N)
O(N)

1 -0 

2 - ? = 1
-1 - ? = 1
-2 - ? = 1
       0 - ? = 1
sorting = O(nlogn)

[-2, -1, 0, 1, 2]
         ^      ^
(-2, 2)
2- -2 = +4
-2 -2 = -4
(-1, 2)
-1  - 2= -3
(2, -1)
2 - -1 = 3

for
  for
    if x-y == k:
      add to result
time: O(N^2)
space = O(N)
[[1, 0], [0, -1], [-1, -2], [2, 1]]


'''