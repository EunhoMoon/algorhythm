"""
https://www.acmicpc.net/problem/17203
"""

import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(Q)]


if N == 1:
    for _ in range(Q):
        print(0)
else:
    diff = [0] * (N - 1)
    for i in range(N - 1):
        diff[i] = abs(arr[i] - arr[i + 1])

    prefix_sum = [0] * (N - 1)
    prefix_sum[0] = diff[0]
    for i in range(1, N - 1):
        prefix_sum[i] = prefix_sum[i - 1] + diff[i]

    results = []
    for l, r in queries:
        if l == r:
            results.append(0)
        else:
            results.append(prefix_sum[r - 2] - (prefix_sum[l - 2] if l > 1 else 0))

    for res in results:
        print(res)
