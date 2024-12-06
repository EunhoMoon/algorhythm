"""
https://www.acmicpc.net/problem/16435
"""

import sys
from collections import deque

input = sys.stdin.readline

fruits_count, bird_length = map(int, input().split())
fruits = deque(sorted(map(int, input().split())))

while fruits:
    fruits_height = fruits.popleft()
    if fruits_height <= bird_length:
        bird_length += 1
    else:
        break

print(bird_length)
