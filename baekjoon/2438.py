"""
https://www.acmicpc.net/problem/2438
"""

N = int(input())

for i in range(N):
    stars = ["*"] * (i + 1)

    print("".join(stars))
