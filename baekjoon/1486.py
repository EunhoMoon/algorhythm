"""
https://www.acmicpc.net/problem/1486
"""

import sys

input = sys.stdin.readline

N = int(input())

swift_scores = list(map(int, input().split()))
semaphore_scores = list(map(int, input().split()))

swift_total = 0
semaphore_total = 0
max_day = 0

for i in range(N):
    swift_total += swift_scores[i]
    semaphore_total += semaphore_scores[i]

    if swift_total == semaphore_total:
        is_same = True
        max_day = i + 1

print(max_day)
