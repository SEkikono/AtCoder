# -*- coding: utf-8 -*-
n= int(input())
h = list(map(int, input().split()))
 
max_hight = h[0]
ans = 1
 
for i in range(n-1):
  if h[i+1] > max_hight :
    max_hight = h[i+1]
    ans = i+2
 
print(ans)
