"""
https://www.acmicpc.net/problem/10810
"""

import sys

input = sys.stdin.readline
N, M = map(int, input().split())

baskets = ["0"] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j + 1):
        baskets[n - 1] = str(k)

print(" ".join(baskets))
