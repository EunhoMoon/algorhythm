"""
https://www.acmicpc.net/problem/2309
"""
import sys
from itertools import combinations

read_input = sys.stdin.readline
dwarfs = [int(read_input()) for _ in range(9)]
real_dwarfs = []

for i in combinations(dwarfs, 7):
    if sum(i) == 100:
        real_dwarfs = list(i)

for dwarf in sorted(real_dwarfs):
    print(dwarf)
