"""
https://www.acmicpc.net/problem/16763
"""

import sys

from collections import deque

input = sys.stdin.readline

N = int(input())
boards = []

for _ in range(N):
    boards.append(list(map(int, input().split())))

is_possible = False

chk = [[False] * N for _ in range(N)]
dq = deque()
dq.append((0, 0))

while dq:
    y, x = dq.popleft()
    num = boards[y][x]
    chk[y][x] = True

    if num == -1:
        is_possible = True
        break
    else:
        if y + num < N and not chk[y + num][x]:
            dq.append((y + num, x))
        if x + num < N and not chk[y][x + num]:
            dq.append((y, x + num))


print("HaruHaru" if is_possible else "Hing")
