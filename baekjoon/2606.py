"""
https://www.acmicpc.net/problem/2606
"""
import sys
from collections import deque

input = sys.stdin.readline

count_of_computers = int(input()) + 1
adj = [[0] * (count_of_computers) for _ in range(count_of_computers)]
check = [[False] * (count_of_computers) for _ in range(count_of_computers)]
contain_root = set([1])

for _ in range(int(input())):
    i, j = map(int, input().split())
    adj[i][j] = 1
    adj[j][i] = 1


def bfs():
    dq = deque()
    dq.append(1)
    global count
    while dq:
        present_node = dq.popleft()
        for next_node in range(1, count_of_computers):
            if adj[present_node][next_node] and not check[present_node][next_node]:
                if present_node in contain_root:
                    contain_root.add(next_node)
                check[present_node][next_node] = True
                dq.append(next_node)


bfs()
print(len(contain_root) - 1)
