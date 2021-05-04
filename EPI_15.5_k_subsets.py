def subsets(arr, k):
  res = []
  
  def backtrack(idx, start, combo):
    if idx == k:
      res.append(combo[:])
      return
    for i in range(start, len(arr)):
      combo.append(arr[i])
      backtrack(idx+1, i+1, combo)
      combo.pop()
    
  backtrack(0, 0, [])
  return res

print(subsets([1, 2, 3, 4, 5], 2))