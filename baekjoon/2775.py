"""
https://www.acmicpc.net/problem/2775
"""

import sys

input = sys.stdin.readline

T = int(input())

apt = [[0] * 15 for _ in range(15)]

for i in range(1, 15):
    apt[0][i] = i


def how_many_pepole_live(k: int, n: int):
    count = 0

    if (k != 0 and n != 0) and not apt[k][n]:
        for i in range(n + 1):
            peoples = how_many_pepole_live(k - 1, i)
            count += peoples

        apt[k][n] = count
    else:
        count = apt[k][n]

    return count


for _ in range(T):
    k = int(input())
    n = int(input())

    if not apt[k][n]:
        how_many_pepole_live(k, n)

    print(apt[k][n])
