"""
https://www.acmicpc.net/problem/31575
"""

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

city = []

for _ in range(M):
    street = list(map(int, input().split()))
    city.append(street)

jinwoo_can_pass = False

dq = deque()
chk = [[False] * N for _ in range(M)]
chk[0][0] = True
dq.append((0, 0))

dy = (0, 1)
dx = (1, 0)


def is_valid_coord(y, x):
    return 0 <= x < N and 0 <= y < M and city[y][x] == 1


while dq:
    y, x = dq.popleft()

    if y == M - 1 and x == N - 1:
        jinwoo_can_pass = True
        break

    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]
        if is_valid_coord(ny, nx) and not chk[ny][nx]:
            chk[ny][nx] = True
            dq.append((ny, nx))

print("Yes" if jinwoo_can_pass else "No")
