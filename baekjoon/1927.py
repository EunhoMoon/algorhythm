"""
https://www.acmicpc.net/problem/1927
 - 시간 복잡도
 - 우선 순위 큐
"""
import sys
import heapq as hq

input = sys.stdin.readline
heap = []

for _ in range(int(input())):
    num = int(input())
    if num == 0:
        print(hq.heappop(heap) if heap else "0")
    else:
        hq.heappush(heap, num)
