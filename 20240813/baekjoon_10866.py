"""
https://www.acmicpc.net/problem/10866
"""

import sys

input = sys.stdin.readline

my_deque = []
for _ in range(int(input())):
    command = input().strip()

    if command.startswith("push_back"):
        my_deque.append(int(command.split(" ")[-1]))
    elif command.startswith("push_front"):
        my_deque.insert(0, int(command.split(" ")[-1]))
    elif command == "pop_front":
        if len(my_deque) == 0:
            print(-1)
        else:
            print(my_deque[0])
            my_deque = my_deque[1:]
    elif command == "pop_back":
        if len(my_deque) == 0:
            print(-1)
        else:
            print(my_deque.pop())
    elif command == "size":
        print(len(my_deque))
    elif command == "empty":
        print(1 if len(my_deque) == 0 else 0)
    elif command == "front":
        print(my_deque[0] if len(my_deque) > 0 else -1)
    else:
        print(my_deque[-1] if len(my_deque) > 0 else -1)
