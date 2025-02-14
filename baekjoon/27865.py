"""
https://www.acmicpc.net/problem/27865
"""

import sys

input = sys.stdin.readline
flush = sys.stdout.flush

N = int(input())

for _ in range(20000):
    print("? 1\n")
    flush()
    result = input().strip()
    if result == "Y":
        print("! 1\n")
        flush()
        sys.exit(0)
    else:
        pass
