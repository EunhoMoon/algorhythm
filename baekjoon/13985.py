"""
https://www.acmicpc.net/problem/17219
"""

import sys

input = sys.stdin.readline

strings = input().split()

if int(strings[0]) + int(strings[2]) == int(strings[-1]):
    print("YES")
else:
    print("NO")
