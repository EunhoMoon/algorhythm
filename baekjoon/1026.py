"""
https://www.acmicpc.net/problem/1026
"""

import sys

input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(
    list(map(int, input().split())),
    reverse=True,
)

result = 0

for i in range(N):
    result += A[i] * B[i]

print(result)
