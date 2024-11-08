"""
https://www.acmicpc.net/problem/1012
"""

import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)


def bfs(y, x, fields, N, M):
    dq = deque([(y, x)])
    fields[y][x] = 0

    while dq:
        py, px = dq.popleft()
        for i in range(4):
            ny = py + dy[i]
            nx = px + dx[i]
            if 0 <= ny < N and 0 <= nx < M and fields[ny][nx]:
                fields[ny][nx] = 0
                dq.append((ny, nx))


for _ in range(T):
    M, N, K = map(int, input().split())
    fields = [[0] * M for _ in range(N)]
    larvas = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        fields[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if fields[i][j]:
                bfs(i, j, fields, N, M)
                larvas += 1

    print(larvas)
