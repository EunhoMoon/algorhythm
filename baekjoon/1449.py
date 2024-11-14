"""
https://www.acmicpc.net/problem/1449
"""
import sys

read_line = sys.stdin.readline
N, L = map(int, read_line().split())

start_pipe: int = 0
result: int = 0

for pipe in sorted(map(int, read_line().split())):
    if not (start_pipe > 0 and pipe - (L - 1) <= start_pipe):
        start_pipe = pipe
        result += 1

print(result)
