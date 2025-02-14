"""
https://www.acmicpc.net/problem/5585
"""

coins = [500, 100, 50, 10, 5, 1]
N = 1000 - int(input())
result = 0

for coin in coins:
    result += N // coin
    N = N % coin
    if N == 0:
        break

print(result)
