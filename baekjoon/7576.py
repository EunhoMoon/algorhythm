"""
https://www.acmicpc.net/problem/7576
"""

import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)


def find_root() -> list:
    global M, N, box
    roots = []
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                roots.append((i, j))

    return roots


def is_valid_coord(y: int, x: int) -> bool:
    global M, N
    return 0 <= y < N and 0 <= x < M


def get_fresh_tomato(visited: list) -> bool:
    global M, N, box

    for i in range(N):
        for j in range(M):
            if box[i][j] == 0 and not visited[i][j]:
                return False

    return True


def bfs(roots: list) -> int:
    global M, N, box
    visited = [[False] * M for _ in range(N)]
    dq = deque()

    for root in roots:
        y, x = root
        dq.append((y, x, 0))
        visited[y][x] = True

    result = 0

    while dq:
        y, x, day = dq.popleft()
        result = max(result, day)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if is_valid_coord(y=ny, x=nx) and box[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                dq.append((ny, nx, day + 1))

    return result if get_fresh_tomato(visited=visited) else -1


roots = find_root()
result = bfs(roots=roots)
print(result)
