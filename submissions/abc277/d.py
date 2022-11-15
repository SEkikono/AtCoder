# -*- coding: utf-8 -*-
n,m = map(int, input().split())
a=sorted(list(map(int, input().split())),reverse=True)
b=set(a)
if len(b)==m or len(b)==1:
  print(0)
  quit()
total=sum(a)
a.extend(a)

point=a[0]
maxa=a[0]
for i in range(1,2*n):
  if a[i-1] == (a[i]+1)%m or a[i-1] == a[i]:
    point+=a[i]
  else:
    point=a[i]
  maxa=max(point,maxa)
print(total-maxa)
