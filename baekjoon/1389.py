"""
https://www.acmicpc.net/problem/1389
"""

import sys

from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

users = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(lambda x: x - 1, map(int, input().split()))
    users[A].append(B)
    users[B].append(A)

kevin = []
result = (-1, N * N)


def bfs(start, goal):
    chk = [False] * N
    chk[start] = True
    dq = deque()
    dq.append((start, 0))

    while dq:
        now, d = dq.popleft()
        if now == goal:
            return d

        nd = d + 1
        for nxt in users[now]:
            if not chk[nxt]:
                chk[nxt] = True
                dq.append((nxt, nd))


def get_kevin(start):
    total = 0

    for i in range(N):
        if i != start:
            total += bfs(start, i)

    return total


for i in range(N):
    kevin.append(get_kevin(i))

for i, v in enumerate(kevin):
    if result[1] > v:
        result = (i, v)

print(result[0] + 1)
