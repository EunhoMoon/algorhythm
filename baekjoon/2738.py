"""
https://www.acmicpc.net/problem/2738
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    arr_sum = []
    for j in range(M):
        arr_sum.append(A[i][j] + B[i][j])

    print(" ".join(map(str, arr_sum)))
