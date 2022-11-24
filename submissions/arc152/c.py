N = int(input())
A = list(map(int, input().split()))
 
M =max(A)
m = min(A)
d = M-m
import math
g = d
for i in A:
    g = math.gcd(g, 2*(i-m))
print(m%g + d)
