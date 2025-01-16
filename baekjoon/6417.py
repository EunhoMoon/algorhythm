"""
https://www.acmicpc.net/problem/6417
"""

import sys

input = sys.stdin.readline

while True:
    N = int(input().strip())
    if N == -1:
        break

    is_possible = False
    max_K = 0

    for K in range(N, 1, -1):
        coconuts = N
        valid = True

        for _ in range(K):
            if (coconuts - 1) % K == 0:
                coconuts = coconuts - 1 - (coconuts - 1) // K
            else:
                valid = False
                break

        if valid and coconuts % K == 0:
            is_possible = True
            max_K = K
            break

    if is_possible:
        print(f"{N} coconuts, {max_K} people and 1 monkey")
    else:
        print(f"{N} coconuts, no solution")
