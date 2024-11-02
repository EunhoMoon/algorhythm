"""
https://www.acmicpc.net/problem/10871
"""

import sys

input = sys.stdin.readline

N, X = map(int, input().split())
A = list(input().split())

print(" ".join(list(filter(lambda x: int(x) < X, A))))
