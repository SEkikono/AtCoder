# -*- coding: utf-8 -*-
N, K, D = map(int, input().split()) #元の数字の個数、何個足すか、割る数
a = list(map(int, input().split()))
# D * K+1 * N+1の3次元配列 
dp = [[[-1 for _ in range(D)] for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 0
for i in range(N):
  for j in range(K+1):
    for k in range(D):
      if dp[i][j][k]==-1:
        continue
      # 大方針として、トップダウンではなくボトムアップで更新していく
      # a_i を選ばない場合の遷移 i,j,kが大きければi+1,j,kを更新していく
      dp[i+1][j][k] = max(dp[i+1][j][k],dp[i][j][k])
      # a_i を選ぶ場合の遷移 i,j,kにa_iを足した場合に、i+1,j+1,k+a_i%dより大きければ更新
      if j!=K:
        dp[i+1][j+1][(k+a[i])%D] = max(dp[i+1][j+1][(k+a[i])%D],dp[i][j][k] + a[i])
print(dp[N][K][0])
