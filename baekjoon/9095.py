"""
https://www.acmicpc.net/problem/9095
"""

import sys

input = sys.stdin.readline

T = int(input())


def fibonacci(num: int, chk: list) -> int:
    if num == 1 or num == 0:
        chk[num] = 1
    if num == 2:
        chk[num] = 2
    if num == 3:
        chk[num] == 4

    if not chk[num]:
        sum_of_num: int = (
            fibonacci(num - 1, chk) + fibonacci(num - 2, chk) + fibonacci(num - 3, chk)
        )
        chk[num] = sum_of_num

    return chk[num]


for _ in range(T):
    n = int(input())
    chk: list = [0] * (n + 1)

    print(fibonacci(n, chk))
