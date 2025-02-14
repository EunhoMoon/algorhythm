"""
https://www.acmicpc.net/problem/10870
"""

import sys

input = sys.stdin.readline

n = int(input())


def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(n))
