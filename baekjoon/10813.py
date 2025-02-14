"""
https://www.acmicpc.net/problem/10813
"""

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
baskets = [i for i in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    first_ball = baskets[a]
    second_ball = baskets[b]
    baskets[a] = second_ball
    baskets[b] = first_ball

print(" ".join(map(str, baskets[1:])))
