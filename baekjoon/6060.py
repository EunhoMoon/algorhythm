"""
https://www.acmicpc.net/problem/6060
"""

import sys

input = sys.stdin.readline

N = int(input())

adj = [0 for _ in range(N)]
arrow = 0

for _ in range(N - 1):
    S, D, i = map(int, input().split())
    adj[S] = i

for i in range(1, len(adj)):
    arrow = 0 if adj[i] + arrow == 2 else adj[i] + arrow

print(arrow)
