"""
https://www.acmicpc.net/problem/2841
"""

import sys

input = sys.stdin.readline

N, P = map(int, input().split())
count = 0

guitar = [[] for _ in range(7)]

for _ in range(N):
    line, flet = map(int, input().split())

    while guitar[line] and guitar[line][-1] > flet:
        guitar[line].pop()
        count += 1

    if guitar[line] and guitar[line][-1] == flet:
        continue

    guitar[line].append(flet)
    count += 1

print(count)
