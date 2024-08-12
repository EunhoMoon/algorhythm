"""
https://www.acmicpc.net/problem/10828
 - 시간 복잡도 최적화 필요
"""

import sys

my_stack = []
input = sys.stdin.readline

for _ in range(int(input())):
    command = input().strip()
    if command.startswith("push"):
        my_stack.append(int(command.split(" ")[-1]))
    elif command == "size":
        print(len(my_stack))
    elif command == "pop":
        print(my_stack.pop() if len(my_stack) > 0 else -1)
    elif command == "empty":
        print(1 if len(my_stack) == 0 else 0)
    else:  # top 명령
        print(my_stack[-1] if len(my_stack) > 0 else -1)
