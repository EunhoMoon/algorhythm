"""
https://www.acmicpc.net/problem/14425
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

S = set()
for _ in range(N):
    S.add(input().rstrip())

count = 0
for _ in range(M):
    if input().rstrip() in S:
        count += 1

print(count)
