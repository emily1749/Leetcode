'''
function indexEqualsValueSearch(A) {
    const key = (i) => A[i] >= i;
    let ans = lowerbound(0, A.length - 1, key);
  
    return (ans === null) ? -1 : (A[ans] === ans) ? ans : -1;
}

function firstOdd(A) {
    const isOdd = (i) => A[i] % 2 === 1;
    return lowerbound(0, A.length - 1, isOdd);
}

function lowerbound(lo, hi, callback) {
    let ans = null;
    while (lo <= hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (callback(mid)) {
            ans = mid;
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    return ans;
}

console.log(indexEqualsValueSearch([-8,0,2,5]));
console.log(indexEqualsValueSearch([-1,0,3,6]));

console.log(firstOdd([0,2,4,8,10,1,2,3,4,5]));
console.log(firstOdd([1,2,3,4,5]));
console.log(firstOdd([0,2,4,8,10]));

'''


def index_equals_value_search(arr):
  #if arr == [0]: return 0
  
  l = 0
  r = len(arr)-1
  lowest_idx = float("inf")
  
  # l = 0
  #r = 3
  while l<=r:
    m = (l+r)//2  # 2  (l+r)/ 2
    if arr[m] == m:
      r = m - 1
      lowest_idx = m
    elif arr[m] < m:
      l = m+1
    else:
      r = m-1
      
  if lowest_idx == float("inf"): 
    return -1
  return lowest_idx

def lowerbound(lo, hi, callback):
    


def index_equals_value_search(A):
  '''
  find first index i in which arr[i] >= i
  '''
  
  ans = None
  lo, hi = 0, len(A) -1
  
  while lo <= hi:
      mid = (lo + hi) // 2
      if A[mid] >= mid: # <------------
          ans = mid
          hi = mid - 1
      else:
          lo = mid + 1
  
  if ans is None:
      return -1
    
  return ans if A[ans] == ans else -1
'''

[2,4,8,10,12,3,7,5,1]
             ^
  
    

              10     
      8             [7]   
    2   4        3     5
          12             1
      
   L                         R
  [2, 8, 4, 12, 10| 3, 7, 5, 1]
                        ^
'''

def find_first_odd_node(root):
    ans = None
    node = root
    
    while node:
        if node.val % 2 == 1:
            ans = node
            node = node.left
        else:
            node = node.right
    return ans
  
  
def find_first_odd(A):
    ans = None
    lo, hi = 0, len(A) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2 # assume node = mid #node.val = A[mid]
        if A[mid] % 2 == 1: # if node.val % 2 == 1:
            ans = mid        #ans = node
            hi = mid - 1     #node = node.left
        else: 
            lo = mid + 1     #node = node.right
    return ans if ans != None else -1




[0]

[0, 1, 2, 3, 4]
l      m      r
       
arr = [-8,0,2,5]

l = 2
r = len(arr)-1    (3)
m = 2
lowest_idx 

m = 1
arr[m] == m: 
  right = m-1
  lowest_idx = m
arr[m] < m:   0 < 1
  left = m +1
else:
  right = m - 1

return lowest_idx
time: O(logN) N lenghth of arr
space: O(1)


'''

for x in [[-8,0,2,5], [-1,0,3,6]]:
  print(index_equals_value_search(x))