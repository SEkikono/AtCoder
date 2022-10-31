# -*- coding: utf-8 -*-
from itertools import product
# 飴の味を入力
tastes = list(map(int, input().split()))
# 箱を作成
box = [[0]*10 for i in range(10)]

# 100回目は適当にLと回答するため、ループは99回まで
for t in range(99):
  cnt = 0
  # 数字を読み取り特定の位置にキャンディを配置
  place = int(input())
  for i,j in product(range(10), repeat=2):
    if box[i][j]==0:
      cnt+=1
      if cnt==place:
        box[i][j]=tastes[t]
        break
  # どの方向に傾けたら次の飴が連結しやすいかを比較する
  # F,B,L,Rの順に、各方向に傾けた場合の連結しやすさ（次の飴と同じ味が何個内側に並ぶか）を数えていく
  indicator=[0,0,0,0]
  # F
  for j in range(10):
    for i in range(10):
      if box[9-i][j] != 0 :
        if box[9-i][j] == tastes[t+1]:
          indicator[0]+=1
        break
  # B
    for i in range(10):
      if box[i][j] != 0: 
        if box[i][j] == tastes[t+1]:
          indicator[1]+=1
        break
  # L
  for i in range(10):
    for j in range(10):
      if box[i][9-j] != 0:
        if box[i][9-j] == tastes[t+1]:
          indicator[2]+=1
        break
  # R
    for j in range(10):
      if box[i][j] != 0 :
        if box[i][j] == tastes[t+1]:
          indicator[3]+=1
        break
  max_dir = 0
  max_ind=indicator[0]
  for i in range(3):
    if indicator[i+1]>max_ind:
      max_dir = i+1
      max_ind=indicator[i+1]
      
  # 出力し、箱を傾けて中身を変える
  if max_dir==0:
    print("F", end = "\n", flush=True) 
    for j in range(10):
      for i in range(9):
        if box[9-i][j] != 0 and box[8-i][j] == 0:
          box[9-i][j], box[8-i][j] = box[8-i][j],box[9-i][j]
  elif max_dir==1:
    print("B", end = "\n", flush=True)
    for j in range(10):
      for i in range(9):
        if box[i][j] != 0 and box[i+1][j] == 0:
          box[i][j], box[i+1][j] = box[i+1][j],box[i][j]
  elif max_dir==2:
    print("L", end = "\n", flush=True)
    for i in range(10):
      for j in range(9):
        if box[i][9-j] != 0 and box[i][8-j] == 0:
          box[8-i][j], box[9-i][j] = box[9-i][j],box[8-i][j]
  else:
    print("R", end = "\n", flush=True)
    for i in range(10):
      for j in range(9):
        if box[i][j] != 0 and box[i][j+1] == 0:
          box[i][j], box[i][j+1] = box[i][j+1],box[i][j]
print("L", end = "\n", flush=True)
