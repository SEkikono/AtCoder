# -*- coding: utf-8 -*-
h,w=map(int, input().split())
s=[['']*h for i in range(w)]
t=[['']*h for i in range(w)]
for i in range(h):
  inp=input()
  for j in range(w):
    s[j][i]=inp[j]
for i in range(h):
  inp=input()
  for j in range(w):
    t[j][i]=inp[j]

s=sorted(s)
t=sorted(t)
if s==t:
  print('Yes')
else:
  print('No')
