"""
https://www.acmicpc.net/problem/11279
"""
import sys
import heapq as hq

input = sys.stdin.readline

numbers = []

for _ in range(int(input())):
    number = int(input())
    if number == 0:
        print(0 if len(numbers) == 0 else -hq.heappop(numbers))
    else:
        hq.heappush(numbers, -number)