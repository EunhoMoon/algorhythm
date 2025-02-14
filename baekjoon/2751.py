"""
https://www.acmicpc.net/problem/2751
"""

import sys
import heapq

input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    heapq.heappush(arr, int(input()))

while arr:
    print(heapq.heappop(arr))
