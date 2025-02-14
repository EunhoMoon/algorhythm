"""
https://www.acmicpc.net/problem/11047
"""
import sys

read_input = sys.stdin.readline

N, K = map(int, read_input().split())
result: int = 0

coins: list = [int(read_input()) for _ in range(int(N))]

for coin in sorted(coins, reverse=True):
    if coin <= K:
        result += K // coin
        K %= coin
    else:
        pass

print(result)
