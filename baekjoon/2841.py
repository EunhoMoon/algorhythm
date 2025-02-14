"""
https://www.acmicpc.net/problem/2841
"""

import sys
from collections import deque

input = sys.stdin.readline

N, P = map(int, input().split())

guitar = [[] for _ in range(7)]
count = 0

for _ in range(N):
    string, fret = map(int, input().split())
    present_string = guitar[string]

    while present_string and present_string[-1] > fret:
        present_string.pop()
        count += 1

    if present_string and present_string[-1] == fret:
        continue

    present_string.append(fret)
    count += 1

print(count)
