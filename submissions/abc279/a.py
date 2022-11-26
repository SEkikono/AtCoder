# -*- coding: utf-8 -*-
s=input()

cnt=0
for i in s:
  if i=='v':
    cnt+=1
  elif i=='w':
    cnt+=2
print(cnt)
