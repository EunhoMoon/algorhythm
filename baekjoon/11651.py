"""
https://www.acmicpc.net/problem/11651
"""

import sys
import heapq

intput = sys.stdin.readline

N = int(input())
coords = []

for _ in range(N):
    X, Y = map(int, input().split())
    heapq.heappush(coords, (Y, X))


while coords:
    Y, X = heapq.heappop(coords)
    print(f"{X} {Y}")
