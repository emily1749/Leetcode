def get_number_of_islands(binaryMatrix):
  def dfs(i, j): 
    if i<0 or j<0 or i>=len(binaryMatrix) or j >=len(binaryMatrix[0]) or binaryMatrix[i][j] == 0:
      return
    binaryMatrix[i][j] = 0
    dfs(i-1, j)
    dfs(i+1, j)
    dfs(i, j-1)
    dfs(i, j+1)
      
  total_islands = 0
  for i in range(len(binaryMatrix)):
    for j in range(len(binaryMatrix[0])):
      if binaryMatrix[i][j] == 1:
        dfs(i, j)
        total_islands+=1
  return total_islands