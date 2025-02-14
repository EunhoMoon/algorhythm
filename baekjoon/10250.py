"""
https://www.acmicpc.net/problem/10250
"""

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    room_number = N // H

    if N % H > 0:
        room_number += 1
        floor = N % H
    else:
        floor = H

    room_number_str = "0" + str(room_number) if room_number < 10 else str(room_number)

    print(f"{floor}{room_number_str}")
