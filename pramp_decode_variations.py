'''
 S = '1262'
 
 time: O(N)
 space: O(N)
 
 dynamic programming
 memoization 
       1262
        /  \
      262   62
      /\   /  \
    62  2
    /\
   2  too big,return
   /\
 result toobig, return
 
hash table = {} previous

pointer for string
count = 0
def dp:
    if pointer>len(S):
      count += 1
      return
    slice1 = S[pointer:pointer+1]
    check slice 1
      dp(pointer+1)
    slice2 = S[pointer:pointer+2]
    check slice 2
    if valid - check less than 26
      dp(pointer+2)

dp(0)

  for loop to run through S(pointer):

base case =
 its fully processed return
recursive step = 
 '''
#S = 1262
#count = 1
#pointer = 1
#slice2= 26
def decodeVariations(S):
  count = 0 
  def dp(pointer):
    if pointer >= len(S):
      count += 1
      return
    dp(pointer+1)
    if pointer < len(S)-1:
      slice2 =int(S[pointer:pointer+2])
      if 10<=slice2<=26:
        dp(pointer+2)
    
  dp(0)
  return count
  
print(decodeVariations('1262'))
  
  
  
"""
def decodeVariations(S):

  if len(S) < 1:
    return 1
  
  first, second = 0, 0
  if 1 <= int(S[0]) <= 9:
    first = decodeVariations(S[1:])

  if 10 <= int(S[:2]) <= 26:
    second = decodeVariations(S[2:])
  
  return first + second
"""
"""
def decodeVariations(s):
    dp = {}
    
    def helper(s, dp):
        # Base Case 1: Empty string
        if not s:
            return 1

        first, second = 0, 0

        if s in dp:
            return dp[s]

        if 1 <= int(s[:1]) <= 9:
            first = helper(s[1:], dp)

        if 10 <= int(s[:2]) <= 26:
            second = helper(s[2:], dp)

        dp[s] = first + second

        return dp[s]
        
    return helper(s, dp)
"""