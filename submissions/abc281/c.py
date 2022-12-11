# -*- coding: utf-8 -*-
n,t = map(int, input().split())
a = list(map(int, input().split()))

t=t%sum(a)
for i in range(len(a)):
  if t < a[i]:
    print(i+1, t)
    break
  else:
    t-=a[i]
