"""
https://www.acmicpc.net/problem/10844
"""

import sys

read_line = sys.stdin.readline
mod = 1_000_000_000

n = int(read_line())
cache = [[0] * 10 for _ in range(n + 1)]  # 초기값 세팅


for i in range(1, 10):
    cache[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j > 0:
            cache[i][j] += cache[i - 1][j - 1]
        if j < 9:
            cache[i][j] += cache[i - 1][j + 1]

for i in cache:
    print(i)

result = 0

for i in range(10):
    result += cache[n][i]

print(result % mod)
