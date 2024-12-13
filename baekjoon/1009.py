"""
https://www.acmicpc.net/problem/1009
"""

import sys

input = sys.stdin.readline

patterns = {
    0: [0],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1],
}

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a %= 10
    pattern = patterns[a]
    length = len(pattern)

    if b == 0:
        print(1)
    else:
        result = pattern[(b - 1) % length]
        print(result if result else 10)
