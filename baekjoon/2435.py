"""
https://www.acmicpc.net/problem/2435
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
max_temp = -100
temps = list(map(int, input().split()))
for i in range(N - K + 1):
    new_max = sum(temps[i : i + K])
    max_temp = max(new_max, max_temp)


print(max_temp)
