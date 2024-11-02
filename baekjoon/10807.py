"""
https://www.acmicpc.net/problem/10807
"""

import sys

input = sys.stdin.readline

N = int(input())
print(list(map(int, input().split())).count(int(input())))
