"""
https://www.acmicpc.net/problem/2563
"""

import sys

input = sys.stdin.readline
N = int(input())
papper = [[0] * 100 for _ in range(100)]
result = 0

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            papper[y + i][x + j] = 1

for i in range(100):
    for j in range(100):
        if papper[i][j]:
            result += 1

print(result)
