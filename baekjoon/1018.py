"""
https://www.acmicpc.net/problem/1158
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [input() for _ in range(N)]
result = N * M  # 충분히 큰 초기 최소 값


def fill(y, x, bw):
    global result
    count = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2:
                if board[y + i][x + j] == bw:
                    count += 1
            else:
                if board[y + i][x + j] != bw:
                    count += 1

    result = min(result, count)


for i in range(N - 7):
    for j in range(M - 7):
        fill(i, j, "B")
        fill(i, j, "W")

print(result)
