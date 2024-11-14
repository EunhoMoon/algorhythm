"""
https://www.acmicpc.net/problem/5430
"""
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    p = input().strip()
    n = int(input())
    arr = input().strip()[1:-1].split(",")

    if n == 0:
        arr = []

    if p.count("D") > n:
        print("error")
        continue

    reverse = False
    left = 0
    right = n

    for command in p:
        if command == "R":
            reverse = not reverse
        elif command == "D":
            if reverse:
                right -= 1
            else:
                left += 1

    if left <= right:
        arr = arr[left:right]
        if reverse:
            arr = arr[::-1]
        print("[" + ",".join(arr) + "]")
    else:
        print("error")
