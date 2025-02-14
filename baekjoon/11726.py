"""
https://www.acmicpc.net/problem/11726
"""

import sys

sys.setrecursionlimit(10**7)

read_line = sys.stdin.readline

n = int(read_line())
cache = [-1] * (n + 1)
cache[1] = 1
cache[2] = 2

for i in range(3, n + 1):
    cache[i] = cache[i - 1] + cache[i - 2]

print(cache[n] % 10_007)
