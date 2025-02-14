"""
https://www.acmicpc.net/problem/4796
"""

import sys

input = sys.stdin.readline
case = 1

while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    print(f"Case {case}: {V // P * L +  min(L, V % P)}")
    case += 1
