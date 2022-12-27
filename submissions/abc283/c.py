# -*- coding: utf-8 -*-
from collections import deque

s =input()
l=len(s)
flag=False

for n in s:
  if int(n)!=0:
    flag=False
  else:
    if flag:
      l-=1
      flag=False
    else:
      flag=True
print(l)
