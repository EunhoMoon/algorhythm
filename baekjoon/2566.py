"""
https://www.acmicpc.net/problem/2566
"""

import sys

input = sys.stdin.readline

max_num = 0
max_nums_coords = (0, 0)

for i in range(1, 10):
    arr = list(map(int, input().split()))
    for j in range(9):
        new_num = arr[j]
        if new_num >= max_num:
            max_num = new_num
            max_nums_coords = (i, j + 1)

print(max_num)
print(f"{max_nums_coords[0]} {max_nums_coords[1]}")
