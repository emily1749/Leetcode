def deletion_distance(str1, str2):
  len_a= len(str1)
  len_b= len(str2)
  result_matrix = [[False for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
  for i in range(len_a+1):
    result_matrix[i][0] = i
  for j in range(len_b+1):
    result_matrix[0][j] = j
    
  for i in range(1, len_a+1):
    for j in range(1, len_b+1):
      if not str1[i-1] == str2[j-1]:
        minimum = min(result_matrix[i-1][j], result_matrix[i][j-1])
        result_matrix[i][j] = minimum + 1
      else:
        result_matrix[i][j] = result_matrix[i-1][j-1]
  return result_matrix[len_a][len_b]
      

'''
str1 = "dog", str2 = "frog"
output: 3

og og

str1 = "some", str2 = "thing"



dynamic programming
2d matrix
  "" f r o g
"" 0 1 2 3 4
d  1 2 3 4 5
o  2 3 4 3 4
g  3 4 5 4 3

fr, d
f, d => 2
fr, "" => 2



min(top, left) +1 if different
if the same: take across left


time:O(a*b) a len of str1, b len str2
space:O(a*b)
'''