"""
https://www.acmicpc.net/problem/2747
"""

dp = {}


def fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    if not n in dp.keys():
        dp[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return dp[n]


print(fibonacci(int(input())))
