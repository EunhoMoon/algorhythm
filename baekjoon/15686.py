"""
https://www.acmicpc.net/problem/15686
"""

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
city = [[] for _ in range(N)]
houses = []
chickens = []

for i in range(N):
    city[i] = list(map(int, input().split()))
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        if city[i][j] == 2:
            chickens.append((i, j))


def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


result = 0


for chicken_comb in combinations(chickens, M):
    total = 0
    for house in houses:
        total += min(get_dist(house, chicken) for chicken in chicken_comb)

    result = min(result, total) if result else total

print(result)
