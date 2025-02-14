"""
https://www.acmicpc.net/problem/17136
"""

import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(10)]
result = 25
pappers = [0] * 6


def is_possible(y, x, size):
    if pappers[size] == 5:
        return False

    if y + size > 10 or x + size > 10:
        return False

    for i in range(size):
        for j in range(size):
            if board[y + i][x + j] == 0:
                return False

    return True


def mark(y, x, size, value):
    for i in range(size):
        for j in range(size):
            board[y + i][x + j] = value

    if value:
        pappers[size] -= 1
    else:
        pappers[size] += 1


def backtracking(y, x):
    global result
    if y == 10:
        result = min(sum(pappers), result)
        return

    if x == 10:
        backtracking(y + 1, 0)
        return

    if board[y][x] == 0:
        backtracking(y, x + 1)
        return

    for size in range(1, 6):
        if is_possible(y, x, size):
            mark(y, x, size, 0)
            backtracking(y, x + 1)
            mark(y, x, size, 1)


backtracking(0, 0)

print(result if result < 25 else -1)
