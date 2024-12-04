"""
https://www.acmicpc.net/problem/2805
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 0, max(trees)
result = 0

while low <= high:
    mid = (low + high) // 2
    sum_tree = 0

    for tree in trees:
        if tree > mid:
            sum_tree += tree - mid
            if sum_tree >= M:
                break

    if sum_tree >= M:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
