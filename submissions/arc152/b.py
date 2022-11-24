import bisect

# -*- coding: utf-8 -*-
n,l = map(int, input().split())
inf=float('inf')
A=[-inf]+list(map(int, input().split()))+[inf]

plus=inf
for a in A[1:n+1]:
  #AにL-aが含まれていた時、調整不要のため2Lが答えとなり、
  #L-aに近い要素について調整が必要な秒数を求めたい
  b=bisect.bisect_right(A, l-a)
  c = b-1
  # a+A[b]>=l, a+A[c]<=lのためabsが不要となる
  plus = min(plus, 2*(a+A[b]-l), 2*(l-a-A[c]))
print(2*l+plus)
