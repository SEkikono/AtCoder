# -*- coding: utf-8 -*-
n,l = map(int, input().split())
a=list(map(int, input().split()))

chair=[0]*n
rest=l
for num in a:
  if rest<2 and num==2:
    print('No')
    quit()
  rest-=(num+1)
print('Yes')
