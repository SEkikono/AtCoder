# -*- coding: utf-8 -*-
# “ü—Í
k= int(input())
s= input()

# ‰ñ“š
if len(s) <= k:
	ans = s
else:
	ans = s[:k] + "..."
print(ans)
