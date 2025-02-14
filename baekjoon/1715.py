"""
https://www.acmicpc.net/problem/1715
"""

import heapq
import sys

input = sys.stdin.readline

N = int(input())

q = []

for _ in range(N):
    heapq.heappush(q, int(input()))

sums = []

while len(q) > 1:
    prev_result = heapq.heappop(q) + heapq.heappop(q)
    heapq.heappush(q, prev_result)
    sums.append(prev_result)

print(sum(sums))
