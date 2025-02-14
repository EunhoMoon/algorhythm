"""
https://www.acmicpc.net/problem/1439
"""

on_zero = 0
on_one = 0

S = input().strip()

prev_zero = False
prev_one = False

for char in S:
    if char == "0":
        if not prev_zero:
            on_zero += 1
        prev_zero = True
        prev_one = False
    else:
        if not prev_one:
            on_one += 1
        prev_one = True
        prev_zero = False

print(min(on_zero, on_one))
