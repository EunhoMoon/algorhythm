"""
https://www.acmicpc.net/problem/24416
"""

n = int(input())
f = [0] * (n + 1)
f[1] = 1
if n > 1:
    f[2] = 1


def fibonacci(n):
    if not f[n]:
        f[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return f[n]


print(f"{fibonacci(n)} {n - 2}")
