"""
https://www.acmicpc.net/problem/10431
"""

import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    input_nums = list(map(int, input().split()))
    students = input_nums[1:]
    count = 0

    new_line = [students[0]]

    for i in range(1, len(students)):
        is_small = False
        for j in range(len(new_line)):
            if students[i] < new_line[j]:
                new_line.insert(j, students[i])
                count += len(new_line) - (j + 1)
                is_small = True
                break
        if not is_small:
            new_line.append(students[i])

    print(f"{input_nums[0]} {count}")
