"""
https://www.acmicpc.net/problem/16099
"""

import sys

input = sys.stdin.readline

T = int(input())
results = []

for i in range(T):
    lt, wt, le, we = map(int, input().split())
    area_telecom = lt * wt
    area_eurecom = le * we

    if area_telecom > area_eurecom:
        results.append("TelecomParisTech")
    elif area_telecom < area_eurecom:
        results.append("Eurecom")
    else:
        results.append("Tie")

print("\n".join(results))
