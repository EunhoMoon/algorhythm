"""
https://www.acmicpc.net/problem/21617
"""

import sys

input = sys.stdin.readline

N = int(input())
h = list(map(int, input().split()))
w = list(map(int, input().split()))

total = 0

for i in range(N):
    total += w[i] * (h[i] + h[i + 1]) / 2

print(total)
