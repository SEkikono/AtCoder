# -*- coding: utf-8 -*-
from collections import deque

n, m = map(int, input().split())
ans=[]
if(m==0):
  for i in range(n):
    ans.append(i+1)
  print(*ans)
  quit()
a=list(map(int, input().split()))

que=deque()
for i in range(n):
  if len(a)!=0 and i+1 == a[0]:
    que.append(a.pop(0))
  else:
    ans.append(i+1)
    while que:
      ans.append(que.pop())
  
print(*ans)
