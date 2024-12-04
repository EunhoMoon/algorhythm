"""
https://www.acmicpc.net/problem/24416
"""

n = int(input())
cnt = n // 5


def dp(n, cnt):
    current_remainder = n - 5 * cnt
    if current_remainder % 2 > 0:
        return dp(n, cnt - 1) if cnt > 0 else -1
    else:
        return cnt + (current_remainder // 2)


print(dp(n, cnt))
