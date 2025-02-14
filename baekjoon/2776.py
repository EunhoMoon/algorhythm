"""
https://www.acmicpc.net/problem/2776
"""

import sys
from bisect import bisect_left

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    note_n = list(map(int, input().split()))
    M = int(input())
    note_m = list(map(int, input().split()))
    note_n.sort()

    for m in note_m:
        idx = bisect_left(note_n, m)
        if idx < N and note_n[idx] == m:
            print(1)
        else:
            print(0)
