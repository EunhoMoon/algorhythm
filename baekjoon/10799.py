"""
https://www.acmicpc.net/problem/10799
"""
import sys

input = sys.stdin.readline

stack = []
count = 0

for idx, bracket in enumerate(input().strip()):
    if bracket == "(":
        stack.append(idx)
    else:
        if stack[-1] == idx - 1:
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1

print(count)