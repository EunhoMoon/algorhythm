"""
https://www.acmicpc.net/problem/5692
"""

import sys
from math import factorial

input = sys.stdin.readline

while True:
    num_str = input().strip()
    if num_str == "0":
        break

    result = 0
    for i in range(len(num_str)):
        result += int(num_str[i]) * factorial(len(num_str) - i)

    print(result)
