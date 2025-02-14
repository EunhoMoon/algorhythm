"""
https://www.acmicpc.net/problem/18870
"""

import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(set(arr))
new_arr = []

for num in arr:
    new_arr.append(bisect_left(sorted_arr, num))

print(" ".join(list(map(str, new_arr))))
