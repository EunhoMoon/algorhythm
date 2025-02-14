"""
https://www.acmicpc.net/problem/9375
"""

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    closet = {}
    for _ in range(n):
        clothes, kind = input().split()
        if kind in closet.keys():
            closet[kind].add(clothes)
        else:
            closet[kind] = set([clothes])

    cases = 1
    for kind in closet:
        cases *= len(closet[kind]) + 1

    print(cases - 1)
