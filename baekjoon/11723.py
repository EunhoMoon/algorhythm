"""
https://www.acmicpc.net/problem/11723
"""
import sys

input = sys.stdin.readline

S = 0
M = int(input())

for _ in range(M):
    command = input().split()
    n = int(command[1]) if len(command) > 1 else 0

    if command[0] == "add":
        S |= (1 << n)
    elif command[0] == "remove":
        S &= ~(1 << n)
    elif command[0] == "check":
        print(1 if S & (1 << n) else 0)
    elif command[0] == "toggle":
        S ^= (1 << n)
    elif command[0] == "all":
        S = (1 << 21) - 1
    else:
        S = 0
