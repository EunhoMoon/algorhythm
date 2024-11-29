"""
https://www.acmicpc.net/problem/2217
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
ropes = deque(sorted([int(input()) for _ in range(N)]))
max_weight = 0

while ropes:
    ropes_len = len(ropes)
    new_rope = ropes.popleft()

    new_max_weight = new_rope * ropes_len
    max_weight = new_max_weight if new_max_weight > max_weight else max_weight

print(max_weight)
