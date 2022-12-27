# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
  r = list(map(int, input().split()))
  if r[0]==1:
    a[r[1]-1]=r[2]
  else:
    print(a[r[1]-1])
