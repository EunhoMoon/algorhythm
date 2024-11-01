"""
https://www.acmicpc.net/problem/11724
"""
import sys
from collections import deque

read_line = sys.stdin.readline

N, M = map(int, read_line().split())
maze = []

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for _ in range(N):
    nodes = list(map(int, read_line().rstrip()))
    maze.append(nodes)

def is_valid_coord(y, x):
    return (0 <= x < M and 0 <= y < N) and maze[y][x] == 1


def bfs():
    checked_list = [[False] * M for _ in range(N)]
    checked_list[0][0] = True

    q = deque()
    q.append((0, 0, 1))

    while len(q) > 0:
        y, x, d = q.popleft() # d = 움직인 횟수

        if y == N - 1 and x == M - 1:
            return d

        nd = d + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and not checked_list[ny][nx]:
                checked_list[ny][nx] = True
                q.append((ny, nx, nd))


print(bfs())
