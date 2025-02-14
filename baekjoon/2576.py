"""
https://www.acmicpc.net/problem/2576
"""

import sys

input = sys.stdin.readline

odd_numbs = []

for _ in range(7):
    num = int(input())

    if num % 2 == 1:
        odd_numbs.append(num)

if odd_numbs:
    print(sum(odd_numbs))
    print(min(odd_numbs))
else:
    print(-1)
