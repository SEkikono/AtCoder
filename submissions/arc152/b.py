import bisect

# -*- coding: utf-8 -*-
n,l = map(int, input().split())
inf=float('inf')
A=[-inf]+list(map(int, input().split()))+[inf]

plus=inf
for a in A[1:n+1]:
  #A��L-a���܂܂�Ă������A�����s�v�̂���2L�������ƂȂ�A
  #L-a�ɋ߂��v�f�ɂ��Ē������K�v�ȕb�������߂���
  b=bisect.bisect_right(A, l-a)
  c = b-1
  # a+A[b]>=l, a+A[c]<=l�̂���abs���s�v�ƂȂ�
  plus = min(plus, 2*(a+A[b]-l), 2*(l-a-A[c]))
print(2*l+plus)
