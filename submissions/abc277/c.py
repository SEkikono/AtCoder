# -*- coding: utf-8 -*-
from collections import defaultdict, deque
n = int(input())
# �����O���t��\�������B���X�g���f�t�H���g�Ƃ��邱�ƂŃL�[�̑��݊m�F���s�v�ƂȂ�
graph = defaultdict(list)
for _ in range(n) :
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

que = deque()
que.append(1)
# 1�K�ƂȂ����Ă���K���L�^����p�̃Z�b�g
S = {1}
# que�̗v�f��������胋�[�v 
while que:
  v = que.popleft()
  # 1�K����Ȃ����Ă��Ȃ��K��s�ɋL�^����Ȃ�
  for i in graph[v]:
    # ���ɋL�^���ꂽ�K��s�ɋL�^����Ȃ�
    if not i in S:
      que.append(i)
      S.add(i)
print(max(S))
