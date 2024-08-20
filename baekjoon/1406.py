"""
https://www.acmicpc.net/problem/1406
"""
import sys
from collections import deque

input = sys.stdin.readline

left = deque(input().strip())
right = deque()

for _ in range(int(input())):
    command = input().strip().split()

    if command[0] == "P":
        left.append(command[1])
    elif command[0] == "L":
        if left:
            right.appendleft(left.pop())
    elif command[0] == "D":
        if right:
            left.append(right.popleft())
    elif command[0] == "B":
        if left:
            left.pop()

print("".join(left) + "".join(right))
