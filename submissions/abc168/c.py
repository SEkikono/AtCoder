# -*- coding: utf-8 -*-
import math

# ����
a, b, h, m= map(float, input().split())

# ��
# �p�x
mdeg = m*360/60
hdeg = h*360/12+mdeg/12
# �e���W�̍�
dx = b*math.cos(math.radians(mdeg))-a*math.cos(math.radians(hdeg))
dy = b*math.sin(math.radians(mdeg))-a*math.sin(math.radians(hdeg))
# ���ʂ��o��
ans = math.sqrt(dx**2.+dy**2.)
print('{:.10f}'.format(ans));
