"""
https://www.acmicpc.net/problem/11050
"""

N, K = map(int, input().split())


def bino(n, k):
    if k == 0 or n == k:
        return 1

    return bino(n - 1, k) + bino(n - 1, k - 1)


print(bino(N, K))
