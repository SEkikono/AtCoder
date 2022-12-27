# -*- coding: utf-8 -*-
from collections import deque

q=deque(input())
memo=set()
while len(q)!=0:
  tmp=q.popleft()
  if tmp=='(':
    pass
  elif tmp==')':
    memo.clear()
  else:
    if tmp in memo:
      print('No')
      quit()
    memo.add(tmp)
print('Yes')
