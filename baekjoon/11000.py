"""
https://www.acmicpc.net/problem/11000
"""

import heapq
import sys

input = sys.stdin.readline

N = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(N)]

lectures.sort()

class_rooms = []

for start, end in lectures:
    if class_rooms and class_rooms[0] <= start:
        heapq.heappop(class_rooms)

    heapq.heappush(class_rooms, end)

print(len(class_rooms))
