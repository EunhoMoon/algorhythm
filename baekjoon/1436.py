"""
https://www.acmicpc.net/problem/1436
"""

import sys

input = sys.stdin.readline

N = int(input())

dooms = []
doom_number = 666

dooms.append(doom_number)

while len(dooms) < N:
    doom_number += 1
    if "666" in str(doom_number):
        dooms.append(doom_number)

print(dooms[N - 1])
