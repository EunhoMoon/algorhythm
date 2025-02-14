"""
https://www.acmicpc.net/problem/1931
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
times = [tuple(map(int, input().split())) for _ in range(N)]

times.sort(key=lambda x: (x[1], x[0]))

end_time = 0
max_time = 0

for start, end in times:
    if start >= end_time:
        max_time += 1
        end_time = end

print(max_time)
