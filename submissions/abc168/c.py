# -*- coding: utf-8 -*-
import math

# 入力
a, b, h, m= map(float, input().split())

# 回答
# 角度
mdeg = m*360/60
hdeg = h*360/12+mdeg/12
# 各座標の差
dx = b*math.cos(math.radians(mdeg))-a*math.cos(math.radians(hdeg))
dy = b*math.sin(math.radians(mdeg))-a*math.sin(math.radians(hdeg))
# 結果を出力
ans = math.sqrt(dx**2.+dy**2.)
print('{:.10f}'.format(ans));
