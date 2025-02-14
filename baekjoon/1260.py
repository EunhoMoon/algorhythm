"""
https://www.acmicpc.net/problem/1260
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

adj = [[] for _ in range(N + 1)]

for _ in range(M):
    start_node, end_node = map(int, input().split())
    adj[start_node].append(end_node)
    adj[end_node].append(start_node)

for nodes in adj:
    nodes.sort()


def dfs(node, result):
    result.append(node)
    for next_node in adj[node]:
        if next_node in adj[node] and next_node not in result:
            dfs(next_node, result)

    return result


def bfs(start_node):
    result = [start_node]
    dq = deque()
    dq.append(start_node)
    while dq:
        present_node = dq.popleft()
        for next_node in adj[present_node]:
            if next_node not in result:
                result.append(next_node)
                dq.append(next_node)
    print(" ".join(map(str, result)))


print(" ".join(map(str, dfs(V, []))))
bfs(V)
