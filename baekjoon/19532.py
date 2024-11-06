"""
https://www.acmicpc.net/problem/19532
"""

import sys

input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    is_find = False
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(f"{x} {y}")
            is_find = True
            break
    if is_find:
        break