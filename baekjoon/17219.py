"""
https://www.acmicpc.net/problem/17219
"""

import sys

input = sys.stdin.readline
N, M = map(int, input().split())

notepad = {}
for _ in range(N):
    site, pw = input().split()
    notepad[site] = pw

for _ in range(0, M):
    print(notepad[input().strip()])
