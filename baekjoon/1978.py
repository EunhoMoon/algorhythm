"""
https://www.acmicpc.net/problem/30802
"""

import sys, math

input = sys.stdin.readline

N = int(input())
count = 0


def find_prime_number(num: int) -> bool:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


for num in map(int, input().split()):
    if num > 1 and find_prime_number(num):
        count += 1

print(count)
