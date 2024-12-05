"""
https://www.acmicpc.net/problem/1049
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

min_package = 1000
min_single = 1000

for _ in range(M):
    package, single = map(int, input().split())
    min_package = min(min_package, package)
    min_single = min(min_single, single)

print(
    min(
        (N // 6 * min_package) + (N % 6 * min_single),
        ((N // 6 + 1) * min_package),
        N * min_single,
    )
)
