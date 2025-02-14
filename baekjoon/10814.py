"""
https://www.acmicpc.net/problem/10814
"""

import sys
import heapq

input = sys.stdin.readline

N = int(input())
member_list = []
name_list = [""] * N

for i in range(N):
    age, name = input().split()

    heapq.heappush(member_list, (int(age), i))
    name_list[i] = name

while member_list:
    age, idx = heapq.heappop(member_list)

    print(f"{age} {name_list[idx]}")
