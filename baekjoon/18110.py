"""
https://www.acmicpc.net/problem/18110
"""

import sys

input = sys.stdin.readline


def round_impl(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(input())

if n:
    opinions = [int(input().strip()) for _ in range(n)]
    opinions.sort()
    idx = round_impl(n * 0.15)
    if idx:
        opinions = opinions[idx:-idx]

    result = round_impl(sum(opinions) / len(opinions))
else:
    result = n

print(result)
