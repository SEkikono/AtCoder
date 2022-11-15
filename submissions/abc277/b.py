# -*- coding: utf-8 -*-
n= int(input())

s=[]
fill=True
for i in range(n):
  s.append(input())
  if s.count(s[i])!=1:
    fill=False
    break
  if not(s[i][0] in ["H","D","C","S"]):
    fill=False
    break
  if not(s[i][1] in ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]):
    fill=False
    break

if fill:
  print("Yes")
else:
  print("No")
