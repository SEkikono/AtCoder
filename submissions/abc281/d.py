# -*- coding: utf-8 -*-
N, K, D = map(int, input().split()) #���̐����̌��A���������A���鐔
a = list(map(int, input().split()))
# D * K+1 * N+1��3�����z�� 
dp = [[[-1 for _ in range(D)] for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 0
for i in range(N):
  for j in range(K+1):
    for k in range(D):
      if dp[i][j][k]==-1:
        continue
      # ����j�Ƃ��āA�g�b�v�_�E���ł͂Ȃ��{�g���A�b�v�ōX�V���Ă���
      # a_i ��I�΂Ȃ��ꍇ�̑J�� i,j,k���傫�����i+1,j,k���X�V���Ă���
      dp[i+1][j][k] = max(dp[i+1][j][k],dp[i][j][k])
      # a_i ��I�ԏꍇ�̑J�� i,j,k��a_i�𑫂����ꍇ�ɁAi+1,j+1,k+a_i%d���傫����΍X�V
      if j!=K:
        dp[i+1][j+1][(k+a[i])%D] = max(dp[i+1][j+1][(k+a[i])%D],dp[i][j][k] + a[i])
print(dp[N][K][0])
