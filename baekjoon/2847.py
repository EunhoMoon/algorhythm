"""
https://www.acmicpc.net/problem/2847
"""

levels = [int(input()) for _ in range(int(input()))]
count = 0

for i in range(len(levels) - 2, -1, -1):
    if levels[i] >= levels[i + 1]:
        decrease = levels[i] - levels[i + 1] + 1
        levels[i] -= decrease
        count += decrease

print(count)
