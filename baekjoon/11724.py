"""
https://www.acmicpc.net/problem/11724
"""
import sys

sys.setrecursionlimit(10 ** 6)
read_line = sys.stdin.readline

node_count, edge_count = map(int, read_line().split())
nodes = [[0] * node_count for _ in range(node_count)]
checked_nodes = [False] * node_count
count = 0

for _ in range(edge_count):
    start_node, end_node = map(lambda x: x - 1, map(int, read_line().split()))
    nodes[start_node][end_node] = nodes[end_node][start_node] = 1 # 무방향 == 양방향

def dfs(present_node):
    for next_node in range(node_count):
        if nodes[present_node][next_node] and not checked_nodes[next_node]:
            checked_nodes[next_node] = True
            dfs(next_node)

for n in range(node_count):
    if not checked_nodes[n]:
        count += 1
        checked_nodes[n] = True
        dfs(n)

print(count)