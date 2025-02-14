"""
https://www.acmicpc.net/problem/9085
"""

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    print(sum(filter(lambda x: x <= 10, list(map(int, input().split())))))
