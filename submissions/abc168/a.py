# -*- coding: utf-8 -*-
# ������1�ʓ���
str = input()
N = int(str[-1])

# ��
if N == 3:
	ans = "bon"
elif N in [0, 1, 6, 8]:
	ans = "pon"
else:
	ans = "hon"
print(ans)
