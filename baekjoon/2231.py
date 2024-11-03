"""
https://www.acmicpc.net/problem/2231
"""

import sys

input = sys.stdin.readline
N = int(input())

result = N
count = 0

for i in range(N, 0, -1):
    sum_num = sum(list(map(int, list(str(i)))))
    constructor = sum_num + i
    if constructor == N:
        result = i
        count += 1

if count == 0:
    result = 0

print(result)
