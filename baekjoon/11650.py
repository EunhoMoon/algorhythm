"""
https://www.acmicpc.net/problem/11650
"""

import sys
import heapq

input = sys.stdin.readline

N = int(input())

coords = []

for _ in range(N):
    x, y = map(int, input().split())
    heapq.heappush(coords, (x, y))

while coords:
    x, y = heapq.heappop(coords)

    print(f"{x} {y}")
