# -*- coding: utf-8 -*-
from itertools import product
# ���̖������
tastes = list(map(int, input().split()))
# �����쐬
box = [[0]*10 for i in range(10)]

# 100��ڂ͓K����L�Ɖ񓚂��邽�߁A���[�v��99��܂�
for t in range(99):
  cnt = 0
  # ������ǂݎ�����̈ʒu�ɃL�����f�B��z�u
  place = int(input())
  for i,j in product(range(10), repeat=2):
    if box[i][j]==0:
      cnt+=1
      if cnt==place:
        box[i][j]=tastes[t]
        break
  # �ǂ̕����ɌX�����玟�̈����A�����₷�������r����
  # F,B,L,R�̏��ɁA�e�����ɌX�����ꍇ�̘A�����₷���i���̈��Ɠ��������������ɕ��Ԃ��j�𐔂��Ă���
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
      
  # �o�͂��A�����X���Ē��g��ς���
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
