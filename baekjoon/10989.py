"""
https://www.acmicpc.net/problem/10989
"""

import sys

input = sys.stdin.readline

N = int(input())
arr = [0] * 10_001

for _ in range(N):
    num = int(input())
    arr[num] += 1

for i in range(1, 10_001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)
