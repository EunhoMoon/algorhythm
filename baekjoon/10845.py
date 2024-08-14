"""
https://www.acmicpc.net/problem/10845
 - 시간 복잡도 최적화 필요
"""

import sys

my_queue = []
input = sys.stdin.readline

for _ in range(int(input())):
    command = input().strip()
    if command.startswith("push"):
        my_queue.append(int(command.split(" ")[-1]))
    elif command == "pop":
        if len(my_queue) == 0:
            print(-1)
        else:
            print(my_queue[0])
            my_queue = my_queue[1:]
    elif command == "size":
        print(len(my_queue))
    elif command == "empty":
        print(1 if len(my_queue) == 0 else 0)
    elif command == "front":
        print(my_queue[0] if len(my_queue) > 0 else -1)
    else:
        print(my_queue[-1] if len(my_queue) > 0 else -1)
