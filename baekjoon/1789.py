"""
https://www.acmicpc.net/problem/1789
"""

S = int(input())
sum = 0
i = 1

while sum <= S:
    sum += i
    if S - sum <= i:
        break
    i += 1

print(i)
