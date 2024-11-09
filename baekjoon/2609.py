"""
https://www.acmicpc.net/problem/2609
"""

import sys

num1, num2 = map(int, input().split())

min_num = max(num1, num2)
max_num = min(num1, num2)

for i in range(min(num1, num2), 1, -1):
    print(i)
    if num1 % i == 0 and num2 % i == 0:
        min_num = min(i, min_num)

print(min_num)
