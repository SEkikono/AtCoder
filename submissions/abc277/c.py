# -*- coding: utf-8 -*-
from collections import defaultdict, deque
n = int(input())
# 無向グラフを表す辞書。リストをデフォルトとすることでキーの存在確認が不要となる
graph = defaultdict(list)
for _ in range(n) :
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

que = deque()
que.append(1)
# 1階とつながっている階を記録する用のセット
S = {1}
# queの要素がある限りループ 
while que:
  v = que.popleft()
  # 1階からつながっていない階はsに記録されない
  for i in graph[v]:
    # 既に記録された階はsに記録されない
    if not i in S:
      que.append(i)
      S.add(i)
print(max(S))
