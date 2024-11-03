"""
https://www.acmicpc.net/problem/4153
"""

import sys

input = sys.stdin.readline

while True:
    sides = list(map(int, input().split()))

    if sum(sides) == 0:
        break

    sides.sort()

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("right")
    else:
        print("wrong")
