"""
https://www.acmicpc.net/problem/2667
"""

import sys

from collections import deque

input = sys.stdin.readline

N = int(input())

map = [list(input().strip()) for _ in range(N)]

dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)

dq = deque()
dq.append((0, 0, 0))  # y, x, count


def is_valid_coords(y, x):
    global N

    return 0 <= y < N and 0 <= x < N


visited = [[False] * N for _ in range(N)]

complex = 1
apt_compexs = {}


def dfs(y, x):
    global visited, map, complex, N

    if y >= N or x >= N:
        return
    print(y, x)

    if map[y][x] == "1":
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if is_valid_coords(ny, nx):
                is_end = False
                for j in range(4):
                    ry = ny + dy[i]
                    rx = nx + dx[i]
                    if is_valid_coords(ry, rx):
                        is_end = map[ry][rx] == "0"
                if is_end:
                    complex += 1
                else:
                    if complex in apt_compexs.keys():
                        apt_compexs[complex] += 1
                    else:
                        apt_compexs[complex] = 1
                visited[ny][nx] = True
    map[y][x] = "0"
    if x == N - 1:
        dfs(y + 1, 0)

    dfs(y, x + 1)


dfs(0, 0)
print(apt_compexs)
