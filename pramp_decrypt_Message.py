def decrypt(word):
  pass # your code goes here


# a - 97
# z - 122
# alphabet -> ascci = ord()
# ascii -> alphabet = chr()
'''

enc[n] = dec[n] + secondStep[n-1] + 26m
dec[n] = enc[n] - secondStep[n-1] - 26m
final_word = []
know first letter = word[0] - 1
secondStep = ascii(word[0]) --- for case 0


for loop run through each letter starting from 1, range len(word)
  ascii(word[i]) ==> enc[n]

  res = ascii(word[i]) - secondStep
  while res<97
    +26
    #97-122
  final_word.append(turn to word(res))
  
 
 return "".join(final_word)
    
 time: O(2N) => O(N)
 space: O(N)
 

O = i - 214 - 26m

26



d    n    o   t  q
100 110 111 116 113



100-1
99
c

c    r   i   m   e
99 114 105 109 101

d
100 

r
100+114 == > 110
214  
final - 26 * factor 
factor = 4

i
100+114+105
final - 26 * factor
factor = 

m
100+114+105+109
final - 26 * factor

e
100+114+105+109+101
final - 26 * factor






'''