"""
https://www.acmicpc.net/problem/11399
"""
import sys

input = sys.stdin.readline

N = int(input())

P = sorted(list(map(int, input().split())))

result = 0
prev_result = 0
total_result = 0

for i in range(N):
    result = result + P[i]
    total_result += result

print(total_result)
