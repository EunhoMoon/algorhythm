"""
https://www.acmicpc.net/problem/10815
"""

import sys

input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().split()))
M = int(input())

result = []
for num in list(map(int, input().split())):
    result.append("1" if num in cards else "0")

print(" ".join(result))
