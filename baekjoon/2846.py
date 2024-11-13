"""
https://www.acmicpc.net/problem/2846
"""

import sys

input = sys.stdin.readline

N = int(input())
Pi = list(map(int, input().split()))

MAX_HEIGHT = 0
UPHILL = [Pi[0]]


def get_uphills_height():
    global MAX_HEIGHT
    global UPHILL

    if len(UPHILL) > 1:
        MAX_HEIGHT = max(UPHILL[-1] - UPHILL[0], MAX_HEIGHT)


for i in range(1, N):
    if Pi[i] > Pi[i - 1]:
        UPHILL.append(Pi[i])
    else:
        get_uphills_height()
        UPHILL = [Pi[i]]

get_uphills_height()

print(MAX_HEIGHT)
