"""
https://www.acmicpc.net/problem/15829
"""

result = 0

N = int(input())
strings = input()

for i in range(N):
    result += (ord(strings[i]) - 96) * (31**i)

print(result % 1234567891)
