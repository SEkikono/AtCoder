# -*- coding: utf-8 -*-
# 整数第1位入力
str = input()
N = int(str[-1])

# 回答
if N == 3:
	ans = "bon"
elif N in [0, 1, 6, 8]:
	ans = "pon"
else:
	ans = "hon"
print(ans)
