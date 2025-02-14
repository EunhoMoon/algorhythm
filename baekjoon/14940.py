"""
https://www.acmicpc.net/problem/14940
"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
adj = [[0] * m for _ in range(n)]

dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)


def find_finish():
    for i in range(n):
        for j in range(m):
            if map[i][j] == 2:
                return (i, j)


finish = find_finish()
finish_y, finish_x = finish

dq = deque()
dq.append((finish_y, finish_x, 0))

chk = [[False] * m for _ in range(n)]
chk[finish_y][finish_x] = True


def is_road(a, b):
    return 0 <= a < n and 0 <= b < m


while dq:
    y, x, count = dq.popleft()

    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x

        if is_road(ny, nx) and map[ny][nx] != 0 and not chk[ny][nx]:
            dq.append((ny, nx, count + 1))
            chk[ny][nx] = True
            adj[ny][nx] = count + 1

for i in range(n):
    for j in range(m):
        if map[i][j] > 0 and adj[i][j] == 0 and (i, j) != finish:
            adj[i][j] = -1

for nodes in adj:
    row = []
    for node in nodes:
        row.append(str(node))

    print(" ".join(row))
