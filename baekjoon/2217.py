"""
https://www.acmicpc.net/problem/2217
"""

import sys
from collections import deque

input = sys.stdin.readline

ropes = deque(sorted([int(input()) for _ in range(int(input()))]))
max_weight = 0

while ropes:
    new_max_weight = ropes.popleft() * (len(ropes) + 1)
    max_weight = new_max_weight if new_max_weight > max_weight else max_weight

print(max_weight)
