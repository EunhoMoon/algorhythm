"""
https://www.acmicpc.net/problem/2798
"""

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_num = 0

for i in combinations(cards, 3):
    new_maxnum = sum(i)
    if new_maxnum <= M:
        max_num = max(new_maxnum, max_num)

print(max_num)
