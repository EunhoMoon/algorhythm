"""
https://www.acmicpc.net/problem/10809
"""

import sys

input = sys.stdin.readline

S = input()

result = []

alphabets = "abcdefghijklmnopqrstuvwxyz"

for alphabet in alphabets:
    result.append(f"{S.find(alphabet)}")

print(" ".join(result))
