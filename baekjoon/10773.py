"""
https://www.acmicpc.net/problem/10773
 - stack 문제
"""

import sys

input = sys.stdin.readline

numbers = []
for _ in range(int(input())):
    num = int(input().strip())
    if num == 0:
        numbers.pop()
    else:
        numbers.append(num)

print(sum(numbers))
