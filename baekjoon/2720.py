"""
https://www.acmicpc.net/problem/2720
"""

coins = [25, 10, 5, 1]

T = int(input())

for _ in range(T):
    result = []
    C = int(input())
    for coin in coins:
        result.append(C // coin)
        C = C % coin

    print(" ".join(map(str, result)))
