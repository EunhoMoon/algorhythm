"""
https://www.acmicpc.net/problem/1259
"""

import sys

while True:
    N = input()
    if int(N) == 0:
        break

    left = 0
    right = len(N) - 1

    is_same = True
    while left <= right:
        if N[left] != N[right]:
            is_same = False
            break
        left += 1
        right -= 1

    print("yes" if is_same else "no")
