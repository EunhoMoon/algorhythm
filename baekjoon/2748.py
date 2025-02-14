"""
https://www.acmicpc.net/problem/2748
"""

import sys

read_line = sys.stdin.readline

n = int(read_line())
cache = [-1] * (n + 1)
cache[0] = 0
cache[1] = 1

for i in range(2, n + 1):
    cache[i] = cache[i - 1] + cache[i - 2]

print(cache[n])
