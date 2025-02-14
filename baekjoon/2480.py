"""
https://www.acmicpc.net/problem/2480
"""

import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

if A == B == C:
    print(10000 + A * 1000)
elif A == B or B == C or A == C:
    num = A if A == B or A == C else C
    print(1000 + num * 100)
else:
    print(max(A, B, C) * 100)
