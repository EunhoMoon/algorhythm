"""
https://www.acmicpc.net/problem/7568
"""

import sys

intput = sys.stdin.readline

N = int(input())

peoples = [tuple(map(int, input().split())) for _ in range(N)]
ranks = [1] * N

for i in range(N):
    for j in range(N):
        if i != j:
            if peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1]:
                ranks[i] += 1

print(" ".join(map(str, ranks)))
