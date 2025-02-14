"""
https://www.acmicpc.net/problem/2292
"""

N = int(input())

count = 1
number = 1

while N > number:
    number += count * 6
    count += 1

print(count)
