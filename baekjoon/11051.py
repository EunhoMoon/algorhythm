"""
https://www.acmicpc.net/problem/11051
"""

import sys

sys.setrecursionlimit(10**7)

read_line = sys.stdin.readline

mod = 10007

cache = [[0] * 1001 for _ in range(1001)]
N, K = map(int, read_line().split())


def bino(n, k):
    if cache[n][k]:
        return cache[n][k]

    if k == 0 or k == n:
        cache[n][k] = 1
    else:
        cache[n][k] = bino(n - 1, k - 1) + bino(n - 1, k)

    return cache[n][k]


print(bino(N, K) % mod)
