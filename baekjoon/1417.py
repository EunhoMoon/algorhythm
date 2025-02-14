"""
https://www.acmicpc.net/problem/1417
"""

import sys

input = sys.stdin.readline
candidates = [int(input()) for _ in range(int(input()))]
count = 0

while True:
    if candidates[0] < max(candidates):
        candidates[candidates.index(max(candidates))] -= 1
        candidates[0] += 1
        count += 1
    else:
        if candidates.count(candidates[0]) > 1:
            count += 1
        break

print(count)
