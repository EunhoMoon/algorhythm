"""
https://www.acmicpc.net/problem/4158
"""

import sys
from bisect import bisect_left

input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 or M == 0:
        break

    arr_n = [int(input()) for _ in range(N)]
    arr_m = [int(input()) for _ in range(M)]
    arr_m.sort()

    result = 0

    for n in arr_n:
        idx = bisect_left(arr_m, n)
        if idx < M and arr_m[idx] == n:
            result += 1

    print(result)
