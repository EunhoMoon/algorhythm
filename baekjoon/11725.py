"""
https://www.acmicpc.net/problem/11047
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(lambda x: x - 1, map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)


def find_parents(tree, N):
    parents = [-1] * N
    visited = [False] * N
    dq = deque([0])
    visited[0] = True

    while dq:
        current = dq.popleft()
        for neighbor in tree[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parents[neighbor] = current + 1
                dq.append(neighbor)
    return parents


print("\n".join(list(map(str, find_parents(tree, N)))[1:]))
