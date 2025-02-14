"""
https://www.acmicpc.net/problem/2525
"""

import sys

input = sys.stdin.readline

A, B = map(int, input().split())
C = int(input())

B = B + C

if B >= 60:
    A = A + (B // 60)
    B = B % 60

if A >= 24:
    A = 0 + (A - 24)

print(f"{A} {B}")
