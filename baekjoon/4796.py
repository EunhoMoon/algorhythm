"""
https://www.acmicpc.net/problem/4796
"""

import sys

input = sys.stdin.readline
case = 1

while True:
    L, P, V = map(int, input().split())
    result = 0

    if L == P == V == 0:
        break

    result = V // P * L + (V % P if V % P < L else L)
    print(f"Case {case}: {result}")
    case += 1
