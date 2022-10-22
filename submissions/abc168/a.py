# -*- coding: utf-8 -*-
# ®”‘æ1ˆÊ“ü—Í
str = input()
N = int(str[-1])

# ‰ñ“š
if N == 3:
	ans = "bon"
elif N in [0, 1, 6, 8]:
	ans = "pon"
else:
	ans = "hon"
print(ans)
