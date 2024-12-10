"""
https://www.acmicpc.net/problem/1697
"""

from collections import deque

N, K = map(int, input().split())

dq = deque()
dq.append(N)

max_num = 100000
visited = [0] * (max_num + 1)

while dq:
    x = dq.popleft()

    if x == K:
        print(visited[x])
        break

    for i in (x + 1, x - 1, x * 2):
        if 0 <= i <= max_num and not visited[i]:
            visited[i] = visited[x] + 1
            dq.append(i)
