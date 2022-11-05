# -*- coding: utf-8 -*-
n,m = map(int,input().split())

arr=[[0] * 0 for i in range(n)]
for i in range(m):
  a,b=map(int, input().split())
  arr[a-1].append(b)
  arr[b-1].append(a)
  
for i in range(n):
  arr[i]=sorted(arr[i])
  size=len(arr[i])
  if(size==0):
    print(0)
  else:
    print(size, *arr[i])
