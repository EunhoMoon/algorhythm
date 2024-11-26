"""
https://www.acmicpc.net/problem/10798
"""

import sys
from collections import deque

input = sys.stdin.readline
arr = []

for _ in range(5):
    arr.append(deque(input().strip()))

string = ""

while any(arr):
    for a in arr:
        if a:
            string += a.popleft()

print(string)
