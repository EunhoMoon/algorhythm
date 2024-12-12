"""
https://www.acmicpc.net/problem/1074
https://velog.io/@mnnnj/%EB%B0%B1%EC%A4%80-1074%EB%B2%88-z-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5-%EC%9E%AC%EA%B7%80
"""

import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())


def Z(N, r, c):
    result = 0

    while N:
        N -= 1

        if r < 2**N and c < 2**N:
            result = result

        if r < 2**N and c >= 2**N:
            result += 2 ** (2 * N)
            c -= 2**N

        if r >= 2**N and c < 2**N:
            result += 2 * (2 ** (2 * N))
            r -= 2**N

        if r >= 2**N and c >= 2**N:
            result += 3 * (2 ** (2 * N))
            r -= 2**N
            c -= 2**N

    return result


print(Z(N, r, c))
