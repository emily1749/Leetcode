def root(x, n):
  lo, hi = 0, x
  while lo <= hi:
    mid = (lo + hi) / 2.0
    powd = pow(mid, n)
    
    if abs(powd - x) < 0.001: #|y ^n - x | < 0.0001
      return mid
    if powd > x:
      hi = mid
    elif powd < x:
      lo = mid
      
# O(log(x) * log(n)) 
# assumine pow is constant here
# O(log(x))
'''
|y ^n - x | < 0.0001

|y-root(x,n)| <  0.0001

|y-root(x,n)| < better epsilon < 0.0001
and they want |y-root(x,n)| < 0.0001

by solving this 
|y ^n - x | < 0.0001, <-----------
your actual 
|y-root(x,n)| < better epsilon < 0.0001

so therefore the answer you solved question where
|y-root(x,n)| <  0.0001

b/c better epsilon < 0.0001
'''
    
    
    

'''              [solution set]
-----------|------ x ^ (1/n) ----- |--------------------
           ^                       ^ 
  actual - 0.001          actual + 0.001
  

you have some y
where y = x ** (1/n)

y ^ n = x
from this observation, y can never be greater than x

search space [0, x]

y ^ n = x
~ in code: approx = pow(y, n)

we can always compare this to x
how far is pow(y, n) from x

if pow(y, n) > x
  then we know that for every y' > y,
  pow(y', n) > x
  so we dont need to check for values > y


input:  x = 9, n = 2
output: 3

lets say that y ~ 4
4 ^ 2 > 9,
5 ^ 2 > 9

2 ^ 2 < 9
1 ^ 2 < 9
0.5555 ^ 2 < 9

x = 9 n = 2
0 -> 9
4.5 ^ n >

|y-root(x,n)| < 0.001)
 ^ these are sqrt value
 
4.5, 3, 9 <-- these are all powered value

y ^n, root(x, n) ^ n


  actual - 0.001          actual + 0.001
  
since y < y ^n
     x ^ (1/n) < x
     
     dist between y^n .. x ^ n (gap is larger)
     0.001 <------- something greater than this
     
    |y ^ n - x | < 0.001
    |y-root(x,n)| < 0.000000001
     


x = 9 n = 2
0 -> 9
4.5 ^ n >

instead of taking |y-root(x,n)| < 0.0001
you can take |y ^n - x | < 0.0001 <-- this gives better answer since its tigher bound

|y ^n - x | < 0.0001
and they want |y-root(x,n)| < 0.0001

by solving this 
|y ^n - x | < 0.0001, <-----------
your actual 
|y-root(x,n)| < better epsilon < 0.0001

so therefore the answer you solved question where
|y-root(x,n)| <  0.0001

b/c better epsilon < 0.0001

'''
