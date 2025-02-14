"""
https://www.acmicpc.net/problem/30802
"""

import sys

input = sys.stdin.readline

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

t_shirts_bundle = 0
pen_bundle = 0
pens = 0

for size in sizes:
    t_shirts_bundle += size // T + 1 if size % T > 0 else size // T

pen_bundle = N // P
pens = N % P

print(t_shirts_bundle)
print(f"{pen_bundle} {pens}")
